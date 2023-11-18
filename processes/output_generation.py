import asyncio
from transformers import AutoTokenizer, BloomForCausalLM

# Setup logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

model_id = "bigscience/bloom-3b"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = BloomForCausalLM.from_pretrained(model_id)

async def generate_text(prompt: str, max_length=200, num_return_sequences=1):
    """
    Generate text based on the provided prompt using the BLOOM model.

    Args:
        prompt (str): The text prompt to generate text from.
        max_length (int): Maximum length of the generated text.
        num_return_sequences (int): Number of sequences to generate.

    Returns:
        list: A list of generated text sequences.
    """
    try:
        # Prepare the prompt
        inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)

        def generate():
            return model.generate(**inputs, max_length=max_length, num_return_sequences=num_return_sequences, do_sample=True)
        
        outputs = await asyncio.to_thread(generate)
        return [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    except Exception as e:
        logger.error(f"An error occurred during text generation: {e}", exc_info=True)
        return []
