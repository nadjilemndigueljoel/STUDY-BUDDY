import json

from google import genai

from config import GEMINI_API_KEY
from prompts import SYSTEM_PROMPT


def get_ai_response(messages):
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is not set in the environment")

    client = genai.Client(api_key=GEMINI_API_KEY)
    conversation = [
        {
            "role": "model" if message["role"] == "assistant" else "user",
            "parts": [{"text": message["content"]}],
        }
        for message in messages
    ] 
    
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=conversation,
        config={
            "system_instruction": (
                SYSTEM_PROMPT
                + " Always use the previous conversation to remember facts about the student."
            ),
            "response_mime_type": "application/json",
        },
    )

    return json.loads(response.text)