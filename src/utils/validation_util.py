from functools import wraps
from flask import request, jsonify

def validate_request(required_fields):
    """
    Decorator to validate request JSON for required fields.
    
    Args:
        required_fields (list): A list of keys that must be in the request payload.
        
    Returns:
        Decorated function that checks the request before execution.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not request.is_json:
                return jsonify({"success": False, "error": "Request must be JSON"}), 400
            
            data = request.get_json()
            missing_fields = [field for field in required_fields if field not in data]
            
            if missing_fields:
                return jsonify({
                    "success": False,
                    "error": f"Missing required fields: {', '.join(missing_fields)}"
                }), 400
            
            return func(*args, **kwargs)
        return wrapper
    return decorator
