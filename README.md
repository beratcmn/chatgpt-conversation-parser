# chatgpt-conversation-parser

Parses ChatGPT conversation links into JSONL files.

## Usage

### Use WebUI

[![Open in Gradio](https://img.shields.io/badge/Gradio-Open%20in%20Gradio-%23F687B3)](https://huggingface.co/spaces/beratcmn/chatgpt-conversation-parser)

This is the easiest way to use the tool. Just click the button above and paste the conversation link to the input box.

### Use CLI

```bash
python chatgpt-conversation-parser.py

"Enter the URL of the conversation to fetch: https://chat.openai.com/share/c08768c7-7b3c-4545-acad-b39069c76768"
```

This will create a JSONL file in the current directory with the conversation data.

## Setup

```bash
pip install -r requirements.txt
```

## TODO

- [x] Add WebUI with Gradio
- [ ] Add support for multiple conversation links
- [ ] Add support for multiple conversation types
