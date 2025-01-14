from src.services.chatbot import IdeaSuggestionChatbot
from src.services.common_utils import sort_ideas_based_on_priority
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table
from rich import print as rprint

def main():
    console = Console()
    console.clear()
    console.print(Panel.fit("Welcome to the App Idea Suggestion Chatbot!", style="bold blue"))
    
    chatbot = IdeaSuggestionChatbot()
    
    # Generate initial ideas
    query = Prompt.ask("""
    💡 Unleash Your Creativity! 💡
    Type in your areas of interest you wish to build an app!
    Whether it's fitness, education, entertainment, or productivity, 
    let your imagination run wild! Share your passions and let's create something amazing together! 🚀\n""")

    if not query.strip():
        query = "What new app should I build?"
    console.print("\n[yellow]Generating ideas...[/yellow]")
    ideas = chatbot.generate_ideas(query)
    
    if not ideas:
        console.print("[red]Failed to generate ideas. Please try again later.[/red]")
        return
    
    # Generate and display priority scores
    console.print("\n[yellow]Generating priority scores...[/yellow]")
    priority_scores = chatbot.generate_priority_scores()
    
    combined_list = sort_ideas_based_on_priority(ideas, priority_scores)

    # Display ideas with priority scores
    console.print("\n[bold green]Generated Ideas sorted based on Priority:[/bold green]")
    # Create a table to display the ideas
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Idea Number", style="dim", width=12)
    table.add_column("Title", style="bold", width=30)
    table.add_column("Description", width=60)
    table.add_column("Priority Score", justify="center", width=15)
    table.add_column("Reasoning", width=60)

    for _, idea in enumerate(combined_list, 1):
        table.add_row(
            str(idea.get('number', 'N/A')),
            idea.get('title', 'Not Found'),
            idea.get('description', 'Not Found'),
            str(idea.get('Priority score', 'Not Found')),
            idea.get('Reasoning', 'Not Found')
        )

    console.print(table)
    
    # Get user selection
    while True:
        selection = Prompt.ask(
            "\nPlease choose two ideas by typing their idea numbers (e.g., '1,3' or '2,1')"
        )
        try:
            selected_indices = [int(x.strip()) for x in selection.split(',')]
            if len(selected_indices) != 2 or not all(1 <= x <= 3 for x in selected_indices):
                raise ValueError()
            break
        except ValueError:
            console.print("[red]Please enter exactly two valid numbers between 1 and 3.[/red]")
    
    # Get and display detailed suggestions
    console.print("\n[yellow]Generating detailed suggestions...[/yellow]")
    detailed_suggestions = chatbot.get_detailed_suggestions(selected_indices)
    
    if detailed_suggestions:
        console.print("\n[bold green]Detailed Suggestions:[/bold green]")
        for idx, suggestion in enumerate(detailed_suggestions):
            title = suggestion.get("title", "Unknown Title")
            key_features = suggestion.get("Key features", [])
            technical_considerations = suggestion.get("Technical considerations", "No technical considerations provided.")
            marketing_strategy = suggestion.get("Marketing strategy", "No marketing strategy provided.")
            development_steps = suggestion.get("Development steps", [])

            # Print each section for the suggestion
            rprint(f"\n[bold]{idx+1}: {title}:[/bold]\n")
            rprint("[bold]Key Features:[/bold]")
            for feature in key_features:
                rprint(f"  - {feature}")

            rprint(f"[bold]Technical Considerations:[/bold]")
            for tech_consideration in technical_considerations:
                rprint(f"  - {tech_consideration}")

            rprint(f"[bold]Marketing Strategy:[/bold]")
            for mark_stat in marketing_strategy:
                rprint(f"  - {mark_stat}")

            rprint("[bold]Development Steps:[/bold]")
            for step in development_steps:
                rprint(f"  - {step}")
    
    console.print("\n[bold blue]Thank you for using the Idea Suggestion Chatbot![/bold blue]")

if __name__ == "__main__":
    main()