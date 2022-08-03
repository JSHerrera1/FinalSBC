import requests


def fetchTerm(term: str) -> list[dict[str, str]]:
    URL = "https://www.wikidata.org/w/api.php?action=query&meta=siteinfo&siprop=namespaces&format=json"

    params = {
        "action": "wbsearchentities",
        "language": "en",
        "format": "json",
        "search": term
    }

    searches = []

    try:
        response = requests.get(URL, params=params)

        for search in response.json()["search"]:
            searches.append({
                "description": search["description"],
                "url": search["url"],
                "label": search["label"],
                "id": search["id"]

            })

    except Exception as e:
        print(e)

    return searches


if __name__ == "__main__":
    responses = fetchTerm('UTPL')

    for response in responses:
        print(response)
