from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup
import groq
import os

app = Flask(__name__)
groq_client = groq.Groq(api_key=("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"))  # Store API key securely


def extract_webpage_text(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    text = soup.get_text(separator='\n')
    lines = [line.strip() for line in text.splitlines()]
    return "\n".join(line for line in lines if line)

def summarize_with_groq(text, model="llama-3.3-70b-versatile"):
    prompt = f"Summarize the following web page content in bullet points:\n\n{text[:12000]}\n\nSummary:"
    response = groq_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )
    return response.choices[0].message.content

def query_summary(text, query, model="llama-3.3-70b-versatile"):
    prompt = f"Based on the following web page content, answer the question: '{query}'\n\n{text[:12000]}\n\nAnswer:"
    response = groq_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )
    return response.choices[0].message.content

@app.route('/', methods=['GET', 'POST'])
def home():
    summary = ""
    mode = ""
    if request.method == 'POST':
        url = request.form.get('url')
        mode = request.form.get('mode')
        query = request.form.get('query')

        try:
            text = extract_webpage_text(url)
            if mode == 'query' and query:
                summary = query_summary(text, query)
            else:
                summary = summarize_with_groq(text)
        except Exception as e:
            summary = f"Error: {str(e)}"

    return render_template('index.html', summary=summary, mode=mode)

if __name__ == '__main__':
    app.run(debug=True)