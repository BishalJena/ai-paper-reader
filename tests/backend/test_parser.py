import pytest
from backend.parser import extract_text_from_pdf, extract_text_from_arxiv
from io import BytesIO

def test_extract_text_from_pdf(tmp_path):
    # create a simple one-page PDF
    from reportlab.pdfgen import canvas
    pdf_path = tmp_path / "test.pdf"
    c = canvas.Canvas(str(pdf_path))
    c.drawString(100, 750, "Hello, World!")
    c.save()

    content = pdf_path.read_bytes()
    text = extract_text_from_pdf(content)
    assert "Hello, World!" in text

def test_extract_text_from_arxiv(monkeypatch):
    # mock requests.get to return known PDF bytes
    import requests
    class Dummy:
        content = b"%PDF-1.4\n%EOF"
    monkeypatch.setattr(requests, "get", lambda url: Dummy())
    text = extract_text_from_arxiv("https://arxiv.org/abs/0000.0000")
    assert isinstance(text, str)
