from flask import Flask, request, jsonify
from flask_cors import CORS
from src.services.chatbot import IdeaSuggestionChatbot
from src.services.common_utils import sort_ideas_based_on_priority

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize chatbot
chatbot = IdeaSuggestionChatbot()

def initialize_routes(app):

    @app.route('/health', methods=['GET'])
    def health_check():
        """Health check endpoint"""
        return jsonify({"status": "healthy"})
    
    @app.route('/generate-ideas', methods=['POST'])
    def generate_ideas():
        """Generate initial ideas"""
        try:
            data = request.get_json()
            query = data.get('query', "What new app should I build?")
            
            # Generate ideas
            ideas = chatbot.generate_ideas(query)
            
            # Generate priority scores
            priority_scores = chatbot.generate_priority_scores()

            combined_list = sort_ideas_based_on_priority(ideas, priority_scores)
            
            return jsonify({
                "combined_list": combined_list
            })
        except Exception as e:
            return jsonify({
                "success": False,
                "error": str(e)
            }), 500
        
    @app.route('/get-suggestions', methods=['POST'])
    def get_suggestions():
        """Get detailed suggestions for selected ideas"""
        try:
            data = request.get_json()
            selected_indices = data.get('selected_indices', [])
            
            if not selected_indices or len(selected_indices) != 2:
                return jsonify({
                    "success": False,
                    "error": "Please select exactly two ideas"
                }), 400
            
            # Get detailed suggestions
            suggestions = chatbot.get_detailed_suggestions(selected_indices)
            
            return jsonify({
                "success": True,
                "suggestions": suggestions
            })
        except Exception as e:
            return jsonify({
                "success": False,
                "error": str(e)
            }), 500
        