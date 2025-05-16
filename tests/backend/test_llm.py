import pytest
from backend.llm import generate_summary_and_code
import nbformat

def test_generate_summary_and_code(monkeypatch):
    dummy_reply = "This is a summary.\n```python\nprint('Hello')\n```"
    class DummyChoice:
        message = {"content": dummy_reply}
    class DummyOpenAI:
        @staticmethod
        def ChatCompletion_create(*args, **kwargs):
            return {"choices": [DummyChoice()]}
    monkeypatch.setattr("openai.ChatCompletion.create", DummyOpenAI.ChatCompletion_create)

    result = generate_summary_and_code("dummy text")
    assert "This is a summary." in result["summary"]
    assert "print('Hello')" in result["code"]
    # validate notebook JSON
    nb = nbformat.reads(result["notebook"], as_version=4)
    assert any(cell.cell_type == 'code' for cell in nb.cells)
