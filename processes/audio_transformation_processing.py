from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import torch
import logging
from typing import Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MODEL_ID = "openai/whisper-large-v3"
DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"
TORCH_DTYPE = torch.float16 if torch.cuda.is_available() else torch.float32
CHUNK_LENGTH_S = 30
BATCH_SIZE = 16
MAX_NEW_TOKENS = 128

# Load model and processor
model = AutoModelForSpeechSeq2Seq.from_pretrained(
    MODEL_ID, torch_dtype=TORCH_DTYPE, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(DEVICE)
processor = AutoProcessor.from_pretrained(MODEL_ID)

# Define pipeline for sound transcription
sound_transcription_model = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    max_new_tokens=MAX_NEW_TOKENS,
    chunk_length_s=CHUNK_LENGTH_S,
    batch_size=BATCH_SIZE,
    return_timestamps=True,
    torch_dtype=TORCH_DTYPE,
    device=DEVICE,
)


async def sound_to_text(sound_bytes: bytes) -> Optional[str]:
    """
    Transcribe sound bytes to text using the Whisper model.

    Args:
        sound_bytes (bytes): Sound data in bytes.

    Returns:
        Optional[str]: Transcribed text or None if an error occurs.
    """
    try:
        if not sound_bytes:
            logger.warning("No sound data provided.")
            return None

        transcription_result = sound_transcription_model(sound_bytes)
        transcription = transcription_result['text'] if transcription_result else "No transcription generated"
        
        return transcription
    except Exception as e:
        logger.error(f"An error occurred during sound transcription: {e}", exc_info=True)
        return None  
