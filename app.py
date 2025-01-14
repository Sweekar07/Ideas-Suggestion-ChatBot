from flask import Flask
from flask_cors import CORS
from src.api.endpoints import initialize_routes

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize API Routes
initialize_routes(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
