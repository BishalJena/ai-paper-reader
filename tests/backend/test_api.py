from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_no_input():
    resp = client.post("/api/upload/")
    assert resp.status_code == 400

def test_upload_pdf(tmp_path, monkeypatch):
    pdf = tmp_path / "a.pdf"
    pdf.write_bytes(b"%PDF-1.4\n%EOF")
    monkeypatch.setattr("backend.parser.extract_text_from_pdf", lambda content: "text")
    monkeypatch.setattr("backend.llm.generate_summary_and_code", lambda text: {"summary": "s", "code":"c", "notebook": "{}"})
    with open(pdf, "rb") as f:
        resp = client.post("/api/upload/", files={"file": f})
    assert resp.status_code == 200
    assert resp.json()["summary"] == "s"
