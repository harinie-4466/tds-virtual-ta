from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional, List
from app.qa_logic import generate_answer
import base64
import io
from PIL import Image

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str
    image: Optional[str] = None

@app.post("/api/")
async def answer_question(payload: QuestionRequest):
    question = payload.question
    if payload.image:
        image_bytes = base64.b64decode(payload.image)
        image = Image.open(io.BytesIO(image_bytes))
        # OCR could be used here (e.g. pytesseract) to extract text
    context = "Pre-scraped course and Discourse content"
    result = generate_answer(question, context)
    return result
