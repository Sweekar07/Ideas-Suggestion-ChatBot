def create_response(data, status_code=200):
    """
    Create a standardized API success response.
    
    Args:
        data (dict): The data to include in the response.
        status_code (int): HTTP status code (default: 200).
        
    Returns:
        Response: A Flask JSON response.
    """
    from flask import jsonify
    return jsonify({
        "success": True,
        "data": data
    }), status_code
