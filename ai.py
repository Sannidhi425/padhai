import time
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash")
MODELS = ["gemini-3.8-flash", "gemini-3.5-flash"]

PROMPT = """You are a friendly teacher helping a college student revise before exams.
Using ONLY the notes below, do this:

1. SIMPLE SUMMARY: explain each topic in very simple language (short points).
2. DAILY LIFE EXAMPLE: for every difficult concept, give one real-life example
   an Indian college student relates to (chai, cricket, bus, mobile, etc.).
3. MEMORY TRICK: give a mnemonic or short-form for key points.
4. IMPORTANT QUESTIONS: list 3 questions of 2 marks, 2 of 5 marks, 1 of 10 marks.

Notes:
{notes}
"""
def generate_summary(text):
    notes = text[:15000]
    last_error = None
    for model in MODELS:
        for attempt in range(4):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=PROMPT.format(notes=notes),
                )
                return response.text
            except Exception as e:
                last_error = e
                time.sleep(4 * (attempt + 1))
    raise last_error

if __name__ == "__main__":
    from extract import extract_text
    
    notes = extract_text("sample.pdf")
    print(generate_summary(notes))