from fastapi import FastAPI, UploadFile, Form
from agents.qa_agent import answer_question
from agents.summary_agent import summarize_text
from agents.mcq_agent import generate_mcqs
from utils.pdf_parser import extract_text_from_pdf, extract_text_from_csv
from utils.vector_store import store_document

app = FastAPI(title="Multi-Agent Document Analysis Bot")

@app.post("/upload/")
async def upload_file(file: UploadFile):
    if file.filename.endswith(".pdf"):
        content = extract_text_from_pdf(file.file)
    elif file.filename.endswith(".csv"):
        content = extract_text_from_csv(file.file)
    else:
        return {"error": "Unsupported file type"}

    store_document(content)
    return {"message": f"{file.filename} processed successfully."}


@app.post("/ask/")
async def ask_question(question: str = Form(...)):
    return {"answer": answer_question(question)}


@app.post("/summarize/")
async def summarize():
    return {"summary": summarize_text()}


@app.post("/generate_mcq/")
async def generate_mcq():
    return {"mcqs": generate_mcqs()}
