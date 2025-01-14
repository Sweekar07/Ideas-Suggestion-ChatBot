import os
import google.generativeai as genai
from rich.console import Console
from src.config.config import priority_prompt, generate_idea_prompt, detailed_suggestion_prompt
import json
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Gemini
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Initialize Rich console
console = Console()

class IdeaSuggestionChatbot:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])

    def generate_ideas(self, query: str) -> json:
        """Generate ideas using Gemini"""
        try:
            response = self.chat.send_message(generate_idea_prompt.format(query=query))            
            json_resp = json.loads(response.text.replace("```", "").replace("json", "").strip())
        except json.JSONDecodeError as e:
            logging.error("JSON Decode Error: %s", e)
            console.print(f"[red]JSON Decode Error: {str(e)}[/red]")
            return []
        except Exception as e:
            console.print(f"[red]Error generating ideas: {str(e)}[/red]")
            return []
        else:
            return json_resp

    def generate_priority_scores(self) -> json:
        """Generate priority scores using Gemini"""
        try:
            response = self.chat.send_message(priority_prompt)
            json_resp = json.loads(response.text.replace("```", "").replace("json", "").strip())
        except Exception as e:
            console.print(f"[red]Error generating priority scores: {str(e)}[/red]")
            return []
        else:
            return json_resp

    def get_detailed_suggestions(self, selected_indices: list) -> json:
        """Get detailed suggestions for selected ideas with improved parsing"""
        try:
            response = self.chat.send_message(detailed_suggestion_prompt.format(ideas=selected_indices))
            json_resp = json.loads(response.text.replace("```", "").replace("json", "").strip())
        except json.JSONDecodeError as e:
            logging.error("JSON Decode Error: %s", e)
            console.print(f"[red]JSON Decode Error: {str(e)}[/red]")
            return []
        except Exception as e:
            console.print(f"[red]Error generating detailed suggestions: {str(e)}[/red]")
            return []
        else:
            return json_resp
        