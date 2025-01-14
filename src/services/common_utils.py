
def sort_ideas_based_on_priority(ideas, priority_scores):
    relevance_dict = {item['title']: item for item in priority_scores}
    combined_list = [
        {**idea, **relevance_dict.get(idea['title'], {})} for idea in ideas
    ]
    return sorted(combined_list, key=lambda x: x.get('Priority score', float('inf')))