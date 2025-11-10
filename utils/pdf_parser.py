import pandas as pd
from io import BytesIO
from pdfminer.high_level import extract_text

def extract_text_from_pdf(file):
    content = extract_text(file)
    return content[:10000]  # limit to first 10k chars for efficiency

def extract_text_from_csv(file):
    df = pd.read_csv(BytesIO(file.read()))
    return df.to_string()
