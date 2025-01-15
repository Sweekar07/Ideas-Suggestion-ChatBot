
generate_idea_prompt = """
    Generate exactly 3 unique and innovative app ideas based on this query: "{query}"
            
    For each idea:
    1. Provide a clear title
    2. Add a brief description
    3. Make it practical and feasible
    
    Format each idea as following structured JSON Schema and return it as an list having dict values:
    [ 
        {{
            "number": int,
            "title": str,
            "description": str,
        }}
    ]

    Guidlines:
    1. Strictly adhere to the JSON format provided above.
    2. Do not include any additional text, explanations, or formatting.
    3. If the user query does not relate to app ideas, return an empty JSON list: []
    """

priority_prompt = """
    Rate these app ideas with priority scores (1-5, where 1 is the highest priority) based on the user's query for app ideas:

    For each idea:
    1. Rate these factors (out of 10): relevance, potential impact, feasibility.
    2. Calculate the overall priority score (1-5): Average the three factors and scale it down.
    3. Provide clear reasoning for relevance, potential impact, and feasibility.

    Use the following JSON format:
    [
        {
            "title": str,
            "Relevance": int,
            "Potential Impact": int,
            "Feasibility": int,
            "Overall Priority Score": int,
            "Reasoning": str
        }
    ]

    Guidelines:
    1. Ensure scores are based on a logical evaluation of relevance, potential impact, and feasibility.
    2. Use clear examples or justifications referencing the original query and app idea.
    3. Strictly adhere to the provided JSON format without additional text or formatting.
    """

detailed_suggestion_prompt = """
    Based on the previous chat response, use these indices to provide detailed suggestions for the selected app ideas: {ideas}.

    For each selected app idea, return detailed suggestions using the following exact JSON schema:
    [
        {{
            "title": "str",
            "Key features": "list of str",
            "Technical considerations": "list of str",
            "Marketing strategy": "list of str",
            "Development steps": "list of str"
        }}
    ]

    Guidelines:
    1. Strictly adhere to the JSON format provided above.
    2. Do not include any additional text, explanations, or formatting.
    3. If the user query does not relate to app ideas, return an empty JSON list: [].
    """
