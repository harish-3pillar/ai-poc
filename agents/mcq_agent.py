import os
from openai import OpenAI
from utils.vector_store import documents

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_mcqs():
    if not documents:
        return "No document loaded yet."

    text = " ".join(documents[:2])
    prompt = f"Create 5 multiple-choice questions with 4 options each based on the following text. Provide the correct answer at the end:\n\n{text}"
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.choices[0].message.content.strip()
