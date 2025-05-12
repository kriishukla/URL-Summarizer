
# URL Summarizer

## Overview
URL Summarizer is a Flask-based AI agent that:
- Accepts a **webpage URL**.
- Extracts textual content from the URL.
- Summarizes the content using **Groq’s LLaMA 3.3-70B model**.
- Supports **two summarization modes**: Full Summary and Query-Based Summary.

This application is ideal for quickly understanding lengthy articles or webpages, especially for research or competitive analysis.

---

## Features

### Accept a URL as Input
- Users can input any valid URL via a clean web interface.

### Retrieve and Analyze Webpage Content
- Uses `requests` to fetch the webpage.
- Parses HTML using `BeautifulSoup` and removes scripts, styles, and non-visible elements.

### Extract Key Information
- Extracts visible text line-by-line.
- Cleans and deduplicates the text for accurate summarization.

### Summarize Using LLM (Groq API)
- Uses Groq’s LLaMA-3.3-70B via `groq` client for:
  - Full summarization.
  - Query-based summarization (contextual response to a user query).

## Run the Flask Application

1.  Ensure you are still in the terminal or command prompt and in the same directory where the `app.py` file is located.
2.  Execute the command to start the Flask development server by one of the followin command based on your python version:
    * python app.py
    * python3 app.py

3.  You should see some output in your terminal indicating that the Flask development server has started. It will typically display a message similar to:

     * Serving Flask app 'app'
     * Debug mode: off
     * Running on [http://127.0.0.1:5000](http://127.0.0.1:5000)
    Press Ctrl+C to quit

    This indicates that the application is now running and accessible on your local machine.

## Application Structure

### app.py
Core backend written using **Flask**.

#### Key Functions:

extract_webpage_text(url)

- Fetches and cleans HTML content using `requests` + `BeautifulSoup`.


summarize_with_groq(text)

- Summarizes webpage in 5–7 bullet points using LLaMA model.


query_summary(text, query)

- Answers specific query based on webpage content.


@route('/', methods=['GET', 'POST'])

- Main route to render form, handle user inputs, and display the summary.

---

### index.html
User interface (Bootstrap-based):
- Text input for URL.
- Radio buttons to select summarization mode.
- Conditional query input.
- Displays summarized output clearly.

---

### style.css
Custom stylesheet to enhance UI appearance:
- Soft colors, clean layout.
- Responsive form and styled summary box.
- Smooth transitions for query input visibility.

---

## 🛠️ Tech Stack

| Component        | Description                                     |
|------------------|-------------------------------------------------|
| **Flask**        | Python micro web framework for app backend.     |
| **Bootstrap 5**  | Frontend styling and responsive layout.         |
| **BeautifulSoup**| HTML parsing and tag filtering.                 |
| **Groq API**     | Access to LLaMA-3.3-70B for AI summarization.   |



