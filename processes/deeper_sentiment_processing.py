from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import logging
from database.schemas.deeper_sentiment_analysis_schema import DeepSentimentScores, DeepSentimentAnalysisCreate

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

model_id = "SamLowe/roberta-base-go_emotions"
deep_sentiment_model = AutoModelForSequenceClassification.from_pretrained(model_id)
deep_sentiment_tokenizer = AutoTokenizer.from_pretrained(model_id)

async def analyze_deep_sentiment(text: str) -> DeepSentimentAnalysisCreate:
    """
    Analyze the sentiment of the given text and return sentiment scores.

    Args:
        text (str): The text to analyze.

    Returns:
        DeepSentimentAnalysisCreate: Object containing sentiment scores.
    """
    try:
        inputs = deep_sentiment_tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        outputs = deep_sentiment_model(**inputs)
        probabilities = torch.sigmoid(outputs.logits).detach().numpy()[0]

        sentiment_dict = dict(zip(DeepSentimentScores.__fields__.keys(), probabilities))

        return DeepSentimentScores(**sentiment_dict)
    except Exception as e:
        logger.error(f"An error occurred during deep sentiment analysis: {e}", exc_info=True)
        return None
