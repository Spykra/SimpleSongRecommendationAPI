from transformers import pipeline
from PIL import Image
import io

image_captioning_model = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")

async def image_to_text(image_bytes: bytes) -> str:
    try:
        # Convert bytes to an Image object
        image = Image.open(io.BytesIO(image_bytes))
        
        caption_result = image_captioning_model(image)
        caption = caption_result[0]['generated_text'] if caption_result else "No caption generated"
        
        return caption
    except Exception as e:
        return f"An error occurred: {e}"
