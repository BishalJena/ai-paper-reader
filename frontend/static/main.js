document.getElementById('upload-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const fileInput = document.getElementById('pdf-input');
  const urlInput = document.getElementById('arxiv-url').value;
  const formData = new FormData();

  if (fileInput.files.length > 0) {
    formData.append('file', fileInput.files[0]);
  } else if (urlInput) {
    formData.append('arxiv_url', urlInput);
  }

  const res = await fetch('/api/upload/', {
    method: 'POST',
    body: formData
  });

  const data = await res.json();
  document.getElementById('summary').innerHTML = `<p>${data.summary}</p>`;

  const codeCell = document.createElement('textarea');
  codeCell.className = "thebelab";
  codeCell.textContent = data.code;
  document.getElementById('notebook-area').appendChild(codeCell);
  thebelab.bootstrap();

  renderPlot(1, 0);
});

function renderPlot(m, c) {
  const x = Array.from({length: 100}, (_, i) => i);
  const y = x.map(xi => m * xi + c);
  Plotly.newPlot('plot', [{ x, y, mode: 'lines+markers' }], { title: 'y = mx + c' });
}

document.getElementById('m-slider').addEventListener('input', (e) => {
  renderPlot(+e.target.value, +document.getElementById('c-slider').value);
});
document.getElementById('c-slider').addEventListener('input', (e) => {
  renderPlot(+document.getElementById('m-slider').value, +e.target.value);
});
