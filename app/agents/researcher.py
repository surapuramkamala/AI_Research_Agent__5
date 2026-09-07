from app.tools.web_search import search_web
from app.tools.webpage_reader import read_webpage
from app.tools.retry import retry_tool


def perform_research(state):

    print("\n[RESEARCHER] Starting research...")

    all_sources = []

    for query in state["search_queries"]:

        print(
            f"\n[RESEARCHER] Processing query: {query}"
        )

        # -----------------------------
        # WEB SEARCH
        # -----------------------------

        search_result = retry_tool(
            search_web,
            query,
            retries=3
        )

        if not search_result["success"]:

            print(
                f"[RESEARCHER] Search failed for: "
                f"{query}"
            )

            continue

        results = search_result["result"]

        print(
            f"[RESEARCHER] Processing "
            f"{len(results)} search results"
        )

        # -----------------------------
        # READ WEBPAGES
        # -----------------------------

        for result in results:

            url = result.get("url", "")

            source = {
                "query": query,
                "title": result.get("title", ""),
                "url": url,
                "snippet": result.get("snippet", ""),
                "content": "",
                "content_status": "snippet_only"
            }

            if not url:

                all_sources.append(source)

                continue

            print(
                f"\n[RESEARCHER] Reading: {url}"
            )

            page_result = retry_tool(
                read_webpage,
                url,
                retries=2
            )

            if page_result["success"]:

                source["content"] = (
                    page_result["result"][:5000]
                )

                source["content_status"] = (
                    "webpage_read"
                )

                print(
                    "[RESEARCHER] Webpage read successfully"
                )

            else:

                # IMPORTANT:
                # Do not fail the research workflow.
                # Keep the search snippet as evidence.

                print(
                    "[RESEARCHER] Could not read webpage. "
                    "Using search snippet instead."
                )

                source["content"] = (
                    source["snippet"]
                )

                source["content_status"] = (
                    "snippet_only"
                )

                source["read_error"] = (
                    page_result.get(
                        "error",
                        "Unknown error"
                    )
                )

            all_sources.append(source)

    state["sources"] = all_sources

    print(
        f"\n[RESEARCHER] Research completed."
    )

    print(
        f"[RESEARCHER] Total sources: "
        f"{len(all_sources)}"
    )

    return state