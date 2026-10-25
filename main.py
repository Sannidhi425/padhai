import os
import shutil
import tempfile

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from extract import extract_text
from ai import generate_summary

app = FastAPI(title="Padhai")


@app.get("/")
def home():
    return FileResponse("index.html")


@app.post("/upload")
def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files allowed")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        shutil.copyfileobj(file.file, tmp)
        path = tmp.name

    text = extract_text(path)
    os.remove(path)

    if len(text.strip()) < 50:
        raise HTTPException(status_code=400, detail="No readable text found. Upload a text-based PDF.")

    try:
        notes = generate_summary(text)
    except Exception:
        raise HTTPException(status_code=503, detail="AI is busy right now. Please try again in a minute.")

    return {
        "filename": file.filename,
        "characters": len(text),
        "preview": text[:300],
        "study_notes": notes,
    }