import ollama


def generate_final_report(state):

    prompt = f"""
You are a professional research report generator.

Generate a validated research report.

TOPIC:
{state["topic"]}

RESEARCH SUMMARY:
{state["summary"]}

FACT CHECK RESULTS:
{state["fact_checks"]}

CRITIC REVIEW:
{state["critic_feedback"]}

AVAILABLE SOURCES:
{state["sources"]}

Rules:

1. Do not include unsupported claims.
2. Clearly mention uncertainty where appropriate.
3. Use evidence-based conclusions.
4. Include the source URLs.
5. Create a professional and structured report.

Use this report structure:

# Executive Summary

# Research Findings

# Evidence and Analysis

# Fact Validation

# Limitations

# Conclusion

# Sources
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

    state["final_report"] = response["message"]["content"]

    return state