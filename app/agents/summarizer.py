import os
import ollama

from dotenv import load_dotenv


load_dotenv()

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.2"
)


def summarize_research(state):

    print("\n[SUMMARIZER] Starting summarization...")

    # Limit the number of sources sent to Ollama
    sources_to_use = state["sources"][:8]

    source_text = ""

    for index, source in enumerate(
        sources_to_use,
        start=1
    ):

        content = source.get(
            "content",
            ""
        )

        snippet = source.get(
            "snippet",
            ""
        )

        # Use only a limited amount of content
        content = content[:1500]

        source_text += f"""

SOURCE {index}

Title:
{source.get("title", "")}

URL:
{source.get("url", "")}

Snippet:
{snippet[:500]}

Content:
{content}
"""

    prompt = f"""
You are a research summarization agent.

Research topic:
{state["topic"]}

Based ONLY on the sources below, create a structured summary.

Do not invent information.

Use this structure:

1. Key Findings
2. Important Facts
3. Areas of Agreement
4. Areas of Disagreement
5. Knowledge Gaps

SOURCES:

{source_text}
"""

    print(
        f"[SUMMARIZER] Sending "
        f"{len(sources_to_use)} sources to Ollama..."
    )

    try:

        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        summary = (
            response["message"]["content"]
        )

        if not summary:

            raise RuntimeError(
                "Ollama returned an empty summary"
            )

        state["summary"] = summary

        print(
            "[SUMMARIZER] Summary generated successfully"
        )

        return state

    except Exception as error:

        print(
            f"[SUMMARIZER] ERROR: "
            f"{type(error).__name__}: {error}"
        )

        raise