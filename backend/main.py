from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse
from backend.parser import extract_text_from_pdf, extract_text_from_arxiv
from backend.llm import generate_summary_and_code
import uvicorn

app = FastAPI()

@app.post("/api/upload/")
async def upload_paper(file: UploadFile = None, arxiv_url: str = Form(None)):
    if file:
        content = await file.read()
        text = extract_text_from_pdf(content)
    elif arxiv_url:
        text = extract_text_from_arxiv(arxiv_url)
    else:
        return JSONResponse(status_code=400, content={"error": "No input provided"})

    response = generate_summary_and_code(text)
    return JSONResponse(content=response)

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000)
