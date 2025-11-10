import os
from openai import OpenAI
from utils.vector_store import documents

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text():
    if not documents:
        return "No document loaded yet."

    text = " ".join(documents)
    prompt = f"Summarize the following text in simple language:\n\n{text}"
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.choices[0].message.content.strip()
