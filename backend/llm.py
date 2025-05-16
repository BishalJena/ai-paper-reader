import openai
import nbformat

openai.api_key = "YOUR_OPENAI_KEY"

def generate_summary_and_code(text: str) -> dict:
    prompt = f"Summarize and implement toy code with visualization for this paper:\n{text[:3000]}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    reply = response['choices'][0]['message']['content']

    summary = reply.split("```")[0]
    code = reply.split("```python")[1].split("```")[0]

    notebook = nbformat.v4.new_notebook()
    notebook.cells = [
        nbformat.v4.new_markdown_cell(summary),
        nbformat.v4.new_code_cell(code)
    ]
    return {
        "summary": summary,
        "code": code,
        "notebook": nbformat.writes(notebook)
    }
