Project Overview

This is a Flask-based API application that provides a system for generating app ideas and detailed suggestions based on user queries. The application uses a chatbot to suggest ideas, sort them based on priority, and provide actionable recommendations.

Features

Health Check Endpoint: Confirm that the app is running.

Idea Generation: Generate unique and innovative app ideas.

Detailed Suggestions: Provide comprehensive suggestions for selected app ideas.

Requirements

To run this project locally, ensure you have the following installed:

pip install -r requirements.txt

Running the Application

Start the Server

Run the application locally:

python app.py

Test the Endpoints

Health Check

Verify the application is running:

curl http://localhost:5000/health

Generate Ideas

Send a POST request to generate app ideas:

curl -X POST -H "Content-Type: application/json" -d "{\"query\": \"What new app should I build?\"}" http://localhost:5000/generate-ideas

Get Suggestions

Get detailed suggestions for selected ideas:



To test the app locally:

Use below commands:

# curl http://localhost:5000/health

# curl -X POST -H "Content-Type: application/json" -d "{\"query\": \"What new app should I build?\"}" http://localhost:5000/generate-ideas

# curl -X POST http://localhost:5000/get-suggestions -H "Content-Type: application/json" -d "{\"selected_indices\": [3,2]}"
