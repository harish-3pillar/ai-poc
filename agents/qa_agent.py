import os
from openai import OpenAI
from utils.vector_store import query_vector_store

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def answer_question(question: str):
    context = query_vector_store(question)
    prompt = f"Answer the question based only on the context below.\n\nContext:\n{context}\n\nQuestion: {question}"
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.choices[0].message.content.strip()

