import gradio as gr
from main import fetch_and_parse_conversation


demo = gr.Interface(
    fn=fetch_and_parse_conversation,
    inputs=["text"],
    outputs=["text", gr.DownloadButton(label="Download JSONL")],
)


demo.launch()
