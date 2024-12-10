import requests
    
class WikipediaSummarization():
    def __init__(
        self,
        min_length_words: int = 250,
        min_length_bytes: int = 1000,
        max_tries: int = 10,
        min_backlinks: int = 1,
    ):
        self.url = "https://en.wikipedia.org/w/api.php"
        self.min_length_words = min_length_words
        self.min_length_bytes = min_length_bytes
        self.max_tries = max_tries
        self.min_backlinks = min_backlinks


    def get_wikipedia_article_content(self, title: str) -> str:
        """Return wikipedia article content

        Args:
            title (str): title of the article
            remove_headers (bool, optional): remove the headers in the content body. Defaults to False.

        Returns:
            str: article content
        """
        # Parameters for the API request to get article content
        params = {
            "action": "query",
            "format": "json",
            "titles": title,
            "prop": "extracts",
            "explaintext": True,  # Get plain text content
        }

        # Making the API request
        # TODO: to avoid blocking from Wikipedia, we should provide a headers argument, where headers = {'User-Agent': 'Bittensor/0.0 (https://Bittensor.org; someone@opentensor.dev)'}
        response = requests.get(self.url, params=params)
        data = response.json()

        # Extracting the page content
        page = next(iter(data["query"]["pages"].values()))
        content = page.get("extract", "Content not found.")

        text = {None: ""}
        section = None
        for line in content.split("\n"):
            if line.startswith("==") and line.endswith("=="):
                section = line.strip("=").strip()
                text[section] = ""
                continue
            text[section] += line + "\n"

        return text[None]
