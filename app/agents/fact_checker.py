import ollama


def fact_check(state):

    prompt = f"""
You are a strict fact checking agent.

Topic:

{state["topic"]}

Summary:

{state["summary"]}

Available sources:

{state["sources"]}

Validate each important claim.

Return structured JSON.

Format:

{{
    "claims": [
        {{
            "claim": "...",
            "status": "SUPPORTED | PARTIALLY_SUPPORTED | UNSUPPORTED",
            "supporting_sources": [
                "source URL"
            ],
            "explanation": "..."
        }}
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

    state["fact_checks"] = (
        response["message"]["content"]
    )

    return state