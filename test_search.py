from ddgs import DDGS


try:
    print("Starting web search...")

    results = DDGS().text(
        "Artificial Intelligence research",
        max_results=5
    )

    for index, result in enumerate(results, start=1):

        print("\n" + "=" * 50)
        print(f"RESULT {index}")
        print("=" * 50)

        print("TITLE:")
        print(result.get("title", ""))

        print("\nURL:")
        print(result.get("href", ""))

        print("\nSNIPPET:")
        print(result.get("body", ""))

except Exception as error:

    print("\nSEARCH FAILED")
    print(type(error).__name__)
    print(str(error))