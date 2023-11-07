from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def enhance_text(content: str) -> str:
    try:

        summarized = summarizer(content, min_length=25, max_length=100)

        return summarized[0]['summary_text']
    except Exception as e:
        return f"An error occurred: {e}"

