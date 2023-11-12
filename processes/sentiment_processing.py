from transformers import AutoModelForSequenceClassification, AutoTokenizer
import numpy as np
from scipy.special import softmax
import logging
from database.schemas.sentiment_analysis_schema import SentimentScores  


# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Sentiment Model and Tokenizer
model_id = "cardiffnlp/twitter-roberta-base-sentiment-latest"
sentiment_model = AutoModelForSequenceClassification.from_pretrained(model_id)
sentiment_tokenizer = AutoTokenizer.from_pretrained(model_id)

async def analyze_sentiment(text: str):
    """
    Analyze the sentiment of the given text.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary with sentiment probabilities.
    """
    try:
        # Preprocess and encode the text for the sentiment model
        inputs = sentiment_tokenizer(text, return_tensors='pt')
        outputs = sentiment_model(**inputs)

        # Apply softmax to the output scores
        probabilities = outputs[0][0].detach().numpy()
        probabilities = softmax(probabilities)

        sentiment_result = SentimentScores(
            negative_score=float(probabilities[0]),
            neutral_score=float(probabilities[1]),
            positive_score=float(probabilities[2]), 
        )

        return sentiment_result
    except Exception as e:
        logger.error(f"An error occurred during sentiment analysis: {e}", exc_info=True)
        return None
