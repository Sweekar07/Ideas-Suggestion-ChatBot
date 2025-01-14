
generate_idea_prompt = """Generate exactly 3 unique and innovative app ideas based on this query: "{query}"
            
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
            3. If the user query does not relate to app ideas, return an empty JSON list: []"""

priority_prompt = """Rate these app ideas with priority scores (1-5, where 1 is highest priority) based on the users query for app ideas:

    For each idea provide:
    1. Priority score (1-5) (based on relevance, potential impact and feasibility for the users query for app ideas)
    2. Brief reasoning (based on relevance, potential impact and feasibility for the users query for app ideas)

    Format as:
    [
        {{
            "title": str,
            "Priority score": int,
            "Reasoning": str
        }}
    ]

    Guidlines:
    1. Strictly adhere to the JSON format provided above.
    2. Do not include any additional text, explanations, or formatting.
    3. If the user query does not relate to app ideas, return an empty JSON list: []
    4. Scoring Logic: Use simple heuristic rules to assign scores (e.g., using keywords or phrases to determine relevance and impact). 
    5. Ensure that the ranking system is intuitive and that explanations for each score are clear. 
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