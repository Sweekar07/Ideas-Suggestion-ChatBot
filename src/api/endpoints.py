from flask import Flask, request, jsonify
import logging
from flask_cors import CORS
from src.services.chatbot import IdeaSuggestionChatbot
from src.services.common_utils import sort_ideas_based_on_priority, format_error_response
from src.utils.response_util import create_response
from src.utils.validation_util import validate_request

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize chatbot
chatbot = IdeaSuggestionChatbot()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_routes(app):

    @app.route('/health', methods=['GET'])
    def health_check():
        """Health check endpoint"""
        return jsonify({"status": "healthy"})
    
    @app.route('/generate-ideas', methods=['POST'])
    @validate_request(["query"])  # Ensures "query" is present in the request
    def generate_ideas():
        """Generate initial ideas"""
        try:
            data = request.get_json()
            query = data.get('query', "What new app should I build?")
            
            logger.info(f"Received query: {query}")

            # Generate ideas
            ideas = chatbot.generate_ideas(query)
            
            # Generate priority scores
            priority_scores = chatbot.generate_priority_scores()
            
        except Exception as e:
            logger.error(f"Error in /generate-ideas: {str(e)}")
            return format_error_response("Failed to generate ideas. Please try again later.")
        else:
            return create_response({"ideas": sort_ideas_based_on_priority(ideas, priority_scores)})
        
    @app.route('/get-suggestions', methods=['POST'])
    @validate_request(["selected_indices"])  # Ensures "selected_indices" is present
    def get_suggestions():
        """Get detailed suggestions for selected ideas"""
        try:
            data = request.get_json()
            selected_indices = data.get('selected_indices', [])
            
            if len(selected_indices) != 2:
                return format_error_response("Please select exactly two ideas", status_code=400)
            
            logger.info(f"Selected indices: {selected_indices}")
            
            # Get detailed suggestions
            suggestions = chatbot.get_detailed_suggestions(selected_indices)
        
        except Exception as e:
            logger.error(f"Error in /generate-ideas: {str(e)}")
            return format_error_response("Failed to generate ideas. Please try again later.")
        else:
            return create_response({"suggestions": suggestions})
        