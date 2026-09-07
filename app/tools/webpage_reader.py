import requests

from bs4 import BeautifulSoup


def read_webpage(url: str):

    print(
        f"[WEBPAGE READER] Reading: {url}"
    )

    headers = {
        "User-Agent": (
            "Mozilla/5.0 "
            "(Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        ),
        "Accept": (
            "text/html,"
            "application/xhtml+xml,"
            "application/xml;q=0.9,"
            "*/*;q=0.8"
        ),
        "Accept-Language": (
            "en-US,en;q=0.9"
        )
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=15
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    # Remove unnecessary elements
    for tag in soup(
        [
            "script",
            "style",
            "nav",
            "footer",
            "header",
            "noscript"
        ]
    ):

        tag.decompose()

    text = soup.get_text(
        separator=" ",
        strip=True
    )

    if not text:

        raise RuntimeError(
            "Webpage contains no readable text"
        )

    return text[:15000]