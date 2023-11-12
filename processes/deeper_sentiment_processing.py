from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import logging
from database.schemas.deeper_sentiment_analysis_schema import DeepSentimentScores


# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

model_id = "SamLowe/roberta-base-go_emotions"
deep_sentimentmodel = AutoModelForSequenceClassification.from_pretrained(model_id)
deep_sentiment_tokenizer = AutoTokenizer.from_pretrained(model_id)

async def analyze_deep_sentiment(text: str) -> DeepSentimentScores:
    """
    Analyze the sentiment of the given text, but in full extent of emotions

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary with sentiment probabilities.
    """
    try:
        inputs = deep_sentiment_tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        outputs = deep_sentimentmodel(**inputs)
        probabilities = torch.sigmoid(outputs.logits).detach().numpy()[0]
        
        # Assuming the order of outputs matches the order in EmotionScores
        return DeepSentimentScores(
            **dict(zip(DeepSentimentScores.__fields__.keys(), probabilities))
        )
    except Exception as e:
        logger.error(f"An error occurred during sentiment analysis: {e}", exc_info=True)
        return None
