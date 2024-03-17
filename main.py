import requests
from bs4 import BeautifulSoup
import json


def fetch_and_parse_conversation(url):
    """
    Fetches a conversation from a given URL and parses it into a JSONL file.

    Args:
        url (str): The URL of the conversation to fetch.

    Returns:
        None
    """

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        script_tag = soup.find(
            "script", attrs={"crossorigin": "anonymous", "id": "__NEXT_DATA__"}
        )

        if script_tag:
            data = json.loads(script_tag.string)
            title = data["props"]["pageProps"]["sharedConversationId"]
            conversation = data["props"]["pageProps"]["serverResponse"]["data"][
                "linear_conversation"
            ]

            formatted_conversation = []

            for i, message in enumerate(conversation):
                if i == 0:
                    continue

                formatted_conversation.append(
                    {
                        "index": i,
                        "id": message["id"],
                        "role": message["message"]["author"]["role"],
                        "text": message["message"]["content"]["parts"][0],
                        "model": data["props"]["pageProps"]["serverResponse"]["data"][
                            "model"
                        ],
                    }
                )
            filename = f"{title}.jsonl"
            with open(filename, "w", encoding="UTF-8") as f:
                for message in formatted_conversation:
                    f.write(json.dumps(message, ensure_ascii=False) + "\n")

            return formatted_conversation, "./" + filename

    else:
        print("Failed to retrieve the content")

    return None


if __name__ == "__main__":
    url = input("Enter the URL of the conversation to fetch: ")
    if url:
        fetch_and_parse_conversation(url)
    else:
        print("URL is required")
