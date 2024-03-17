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

            with open(f"{title}.jsonl", "w", encoding="UTF-8") as f:
                for message in formatted_conversation:
                    f.write(json.dumps(message, ensure_ascii=False) + "\n")

    else:
        print("Failed to retrieve the content")


if __name__ == "__main__":
    fetch_and_parse_conversation(
        "https://chat.openai.com/share/c99f8926-c38b-4e37-a61f-3d6dae649cff"
    )
