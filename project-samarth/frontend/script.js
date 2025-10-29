const askBtn = document.getElementById('ask');
const qBox = document.getElementById('q');
const ans = document.getElementById('ans');

askBtn.onclick = async () => {
  const q = qBox.value;
  ans.textContent = 'Thinking...';
  const res = await fetch('http://localhost:8000/ask', {
    method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify({question:q})
  });
  const data = await res.json();
  ans.textContent = data.answer + '\n\n(raw JSON)\n' + JSON.stringify(data.raw, null, 2);
}
