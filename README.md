# App Idea Generator

A Flask-based API application that leverages advanced chatbot capabilities to generate innovative app ideas and provide detailed suggestions based on user queries. The system helps developers brainstorm and prioritize new application concepts based on feasibility and market potential.

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Requirements](#requirements)
- [Usage](#usage)
  - [Running via CLI](#running-via-cli)
  - [Running via Flask Server](#running-via-flask-server)
- [API Endpoints](#api-endpoints)
- [Examples](#examples)
  

## ✨ Features

- **Health Check Endpoint**: Monitor application is up and running
- **Idea Generation**: Generate unique and innovative app ideas based on user requirements
- **Smart Prioritization**: Sort ideas based on market potential and feasibility
- **Detailed Suggestions**: Get comprehensive recommendations for selected app ideas
- **Dual Interface**: Run via CLI or REST API based on your needs

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/Sweekar07/Ideas-Suggestion-ChatBot.git

```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📝 Requirements

- Python 3.10+
- Flask
- Requests
- Rich
- python-dotenv

Dependencies can be installed using the requirements.txt file:

## 💻 Usage

### Running via CLI

You can run the application directly from the command line:

```bash
python cli.py
```

This will start an interactive session where you can:
1. Input your app idea requirements
2. Get generated ideas
3. Select ideas for detailed suggestions
4. View suggestions

### Running via Flask Server

Start the Flask server:

```bash
python app.py
```

The server will start at `http://localhost:5000`

## 🔌 API Endpoints

### 1. Health Check
Verify the application is running:

```bash
curl http://localhost:5000/health
```

Expected Response:
```json
{
    "status": "healthy",
}
```

### 2. Generate Ideas
Generate app ideas based on user queries:

```bash
curl -X POST \
  http://localhost:5000/generate-ideas \
  -H "Content-Type: application/json" \
  -d '{"query": "What new app should I build?"}'
```

Expected Response:
```json
{
    "ideas": [
        {
          "Priority score": 1,
          "Reasoning": "Highly relevant to financial management, significant potential impact on financial health, feasible with existing technology and financial data sources.",
          "description": "An intuitive financial management app that combines budgeting, investment tracking, and personalized financial advice. It empowers users to make informed financial decisions, save money, and reach their financial goals.",
          "number": 2,
          "title": "FinSight"
        },
        {
          "Priority score": 2,
          "Reasoning": "Relevant to self-improvement, potential impact on health and well-being, feasible with existing technology.",
          "description": "A personalized habit-tracking app that uses AI to provide tailored recommendations, track progress, and offer rewards for achieving goals, promoting healthy habits and self-improvement.",
          "number": 1,
          "title": "SmartHabit"
        },
        {
          "Priority score": 3,
          "Reasoning": "Relevant to education, potential impact on improving learning experiences, may require further development of immersive technology for full feasibility.",
          "description": "A virtual learning platform that connects students and educators in an immersive 3D environment. It offers interactive lessons, virtual field trips, and collaborative learning experiences, enhancing the educational journey and making learning more engaging and accessible.",
          "number": 3,
          "title": "EduVerse"
        }
    ]
}
```

### 3. Get Suggestions
Get detailed suggestions for selected ideas:

```bash
curl -X POST \
  http://localhost:5000/get-suggestions \
  -H "Content-Type: application/json" \
  -d '{"selected_indices": [3,2]}'
```

Expected Response:
```json
{
  "success": true,
  "suggestions": [
    {
      "Development steps": [
        "Define the app's core features and user interface",
        "Develop the backend infrastructure for data storage and processing",
        "Integrate with financial APIs and data sources",
        "Implement AI algorithms for personalized financial advice",
        "Design and develop the user interface for mobile and web platforms",
        "Test and iterate on the app's functionality and user experience",
        "Deploy and maintain the app on app stores and web platforms"
      ],
      "Key features": [
        "Personalized budgeting and expense tracking",
        "Investment tracking and analysis",
        "AI-powered financial advice and insights",
        "Integration with financial accounts and services",
        "User-friendly interface and intuitive design"
      ],
      "Marketing strategy": [
        "Target audience: individuals and families looking to improve their financial management",
        "Content marketing: create valuable content on financial literacy, budgeting, and investment strategies",
        "Partnerships with financial institutions and advisors",
        "Social media marketing and influencer outreach",
        "App store optimization (ASO) for discoverability"
      ],
      "Technical considerations": [
        "Secure and reliable data storage and encryption",
        "Integration with financial APIs and data sources",
        "Scalable and efficient backend infrastructure",
        "Cross-platform compatibility (iOS, Android, web)",
        "Compliance with financial regulations and standards"
      ],
      "title": "FinSight"
    },
    {
      "Development steps": [
        "Design and develop the 3D virtual world and user interface",
        "Create interactive lessons and simulations",
        "Integrate with educational content and resources",
        "Implement collaborative learning tools and social features",
        "Develop cross-platform compatibility for different devices and platforms",
        "Test and iterate on the app's functionality and user experience",
        "Deploy and maintain the app on app stores and web platforms"
      ],
      "Key features": [
        "Immersive 3D virtual learning environment",
        "Interactive lessons and simulations",
        "Virtual field trips and guest lectures",
        "Collaborative learning tools and social interaction",
        "Personalized learning pathways and progress tracking"
      ],
      "Marketing strategy": [
        "Target audience: students, educators, and educational institutions",
        "Showcase the unique and immersive learning experience",
        "Partner with schools, universities, and educational organizations",
        "Create engaging content and demos to demonstrate the app's capabilities",
        "Utilize social media and online communities to generate buzz"
      ],
      "Technical considerations": [
        "Development of a robust 3D virtual world",
        "Optimization for real-time interaction and collaboration",
        "Integration with educational content and resources",
        "Cross-platform compatibility (VR headsets, mobile devices, web)",
        "Scalable and reliable infrastructure to support a large number of users"
      ],
      "title": "EduVerse"
    }
  ]
}
```

## 📝 Examples

### CLI Example
```bash
$ python cli.py

Welcome to App Idea Generator!
Enter your query: I want to build a fitness app
Generating ideas...

Generated Ideas:
1. AI Personal Trainer
2. Meal Prep Assistant
3. Workout Buddy Finder

Select ideas for detailed suggestions (comma-separated numbers): 1,2
Generating detailed suggestions...
[Detailed suggestions will be displayed]
```

### API Example with Python Requests
```python
import requests

# Generate Ideas
response = requests.post('http://localhost:5000/generate-ideas',
    json={'query': 'fitness app ideas'})
ideas = response.json()
print(ideas)

# Get Suggestions
suggestions = requests.post('http://localhost:5000/get-suggestions',
    json={'selected_indices': [1, 2]})
print(suggestions.json())
```
