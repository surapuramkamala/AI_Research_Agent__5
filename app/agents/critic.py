import ollama


def critique_research(state):

    prompt = f"""
You are a critical research reviewer.

Review the following research.

TOPIC:

{state["topic"]}

SUMMARY:

{state["summary"]}

FACT CHECKS:

{state["fact_checks"]}

Identify:

1. Unsupported claims
2. Missing research areas
3. Contradictory information
4. Weak sources
5. Possible hallucinations
6. Recommendations

Return JSON:

{{
    "quality_score": 0,
    "issues": [],
    "recommendations": [],
    "needs_more_research": true
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

    state["critic_feedback"] = (
        response["message"]["content"]
    )

    return state