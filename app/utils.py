import re

def extract_story_details(transcription: str):
    # Regular expressions to find name and genre in the transcription
    name_pattern = r"Name is (\w+)"
    genre_pattern = r"Genre is (\w+)"

    # Extracting details using regular expressions
    name_match = re.search(name_pattern, transcription)
    genre_match = re.search(genre_pattern, transcription)

    # Extracted details
    name = name_match.group(1) if name_match else "Unknown"
    genre = genre_match.group(1) if genre_match else "Unknown"

    return {"name": name, "genre": genre}
