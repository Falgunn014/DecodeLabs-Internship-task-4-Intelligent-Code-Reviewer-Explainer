from google import genai

from config import API_KEY
from config import MODEL_NAME

from prompt import SYSTEM_PROMPT


client = genai.Client(
    api_key=API_KEY
)


def review_code(code):

    final_prompt = f"""
{SYSTEM_PROMPT}

Source Code

{code}
"""

    response = client.models.generate_content(

        model=MODEL_NAME,

        contents=final_prompt

    )

    return response.text