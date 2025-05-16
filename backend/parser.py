import pdfplumber
import requests
from io import BytesIO

def extract_text_from_pdf(content: bytes) -> str:
    with pdfplumber.open(BytesIO(content)) as pdf:
        return "\n".join(page.extract_text() or "" for page in pdf.pages)

def extract_text_from_arxiv(url: str) -> str:
    pdf_url = url.replace("abs", "pdf") + ".pdf"
    response = requests.get(pdf_url)
    return extract_text_from_pdf(response.content)
