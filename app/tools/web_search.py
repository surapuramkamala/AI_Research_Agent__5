from ddgs import DDGS


def search_web(query: str, max_results: int = 5):
    """
    Search the web using DDGS.
    """

    print(f"\n[WEB SEARCH] Searching for: {query}")

    results = []

    ddgs = DDGS()

    search_results = ddgs.text(
        query,
        max_results=max_results
    )

    for result in search_results:

        results.append({
            "title": result.get("title", ""),
            "url": result.get("href", ""),
            "snippet": result.get("body", "")
        })

    print(
        f"[WEB SEARCH] Found {len(results)} results"
    )

    if not results:

        raise RuntimeError(
            f"No search results found for query: {query}"
        )

    return results