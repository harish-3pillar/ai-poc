
# POC Multi-Agent PDF & CSV LLM Project

This project demonstrates how to:
- Upload and process PDF/CSV files
- Use embeddings and FAISS to store and retrieve document chunks
- Implement multi-agent behavior for:
  1. Question Answering
  2. Summarization
  3. MCQ Generation

## Setup
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
```

## API Endpoints
- `/upload/` : Upload PDF/CSV
- `/ask/` : Ask a question
- `/summarize/` : Get summary
- `/generate_mcq/` : Generate MCQs
