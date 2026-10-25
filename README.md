# Padhai

AI-powered exam revision assistant. Upload your college notes or syllabus PDF and get simple summaries, daily-life examples, memory tricks and important questions, ready for last-minute revision.

## Features

- Upload a text-based PDF of your notes
- Simple, easy-to-understand summary of each topic
- Real-life examples for difficult concepts
- Mnemonics and memory tricks
- Important questions (2, 5 and 10 marks)
- Retry and fallback handling when the AI service is busy

## Tech Stack

- Python, FastAPI
- pdfplumber (PDF text extraction)
- Google Gemini API
- HTML, CSS, JavaScript (frontend)

## How It Works

PDF upload, text extraction, AI processing, study notes shown on the page.

## Run Locally

1. Clone the repo and open the folder

```
git clone https://github.com/Sannidhi425/padhai.git
cd padhai
```

2. Create and activate a virtual environment

```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Create a `.env` file (copy `.env.example`) and add your Gemini API key

```
GEMINI_API_KEY=your_api_key_here
```

5. Start the server

```
uvicorn main:app --reload
```

6. Open `http://127.0.0.1:8000` in your browser

## Limitations

- Works with text-based PDFs only (scanned image PDFs are not supported yet)
- Very long notes are truncated before being sent to the AI

## Future Improvements

- Quiz and flashcards from notes
- Day-wise study plan based on exam date
- OCR support for scanned PDFs
- User login and saved history