from sqladmin import ModelView
from database.models import DeepSentimentAnalysis, TextGeneration 

class DeepSentimentAnalysisAdmin(ModelView, model=DeepSentimentAnalysis):
    column_list = [
        'id', 'text_id', 'admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring', 
        'confusion', 'curiosity', 'desire', 'disappointment', 'disapproval', 'disgust', 
        'embarrassment', 'excitement', 'fear', 'gratitude', 'grief', 'joy', 'love', 'nervousness',
        'optimism', 'pride', 'realization', 'relief', 'remorse', 'sadness', 'surprise', 'neutral'
    ]


class TextGenerationAdmin(ModelView, model=TextGeneration):
    column_list = ['id', 'original_text', 'generated_text']

