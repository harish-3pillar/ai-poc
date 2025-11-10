import os
import numpy as np
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

documents = []
embeddings = []

def store_document(text):
    global documents, embeddings
    documents.clear()
    embeddings.clear()
    documents.extend([text[i:i+1000] for i in range(0, len(text), 1000)])
    embeddings.extend([get_embedding(chunk) for chunk in documents])

def get_embedding(text):
    resp = client.embeddings.create(model="text-embedding-3-small", input=text)
    return np.array(resp.data[0].embedding)

def query_vector_store(query):
    if not documents:
        return "No document uploaded yet."
    q_emb = get_embedding(query)
    sims = [np.dot(q_emb, e) / (np.linalg.norm(q_emb) * np.linalg.norm(e)) for e in embeddings]
    best_idx = int(np.argmax(sims))
    return documents[best_idx]
