from transformers import pipeline


sound_transcription_model = pipeline("automatic-speech-recognition",model="openai/whisper-large-v2")

async def sound_to_text(sound_bytes: bytes) -> str:
    try:

        transcription_result = sound_transcription_model(sound_bytes)
        transcription = transcription_result['text'] if transcription_result else "No transcription generated"
        
        return transcription
    except Exception as e:
        return f"An error occurred: {e}"
