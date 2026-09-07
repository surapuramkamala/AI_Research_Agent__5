import json
import ollama


def create_plan(topic: str):

    prompt = f"""
You are a research planning agent.

Create a research plan for the topic:

{topic}

Return ONLY valid JSON.

Format:

{{
    "research_questions": [
        "question 1",
        "question 2"
    ],
    "search_queries": [
        "query 1",
        "query 2",
        "query 3"
    ]
}}
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response["message"]["content"]

    return json.loads(content)