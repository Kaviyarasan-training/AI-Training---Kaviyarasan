# Email Reply Assistant with Ollama

This capstone project builds an email reply assistant using Python, a local Ollama model, and a simple Streamlit web UI. The system generates professional replies from an input email without using proprietary APIs.

## Features
- Uses open-source models locally through Ollama
- Supports multiple prompt strategies: zero-shot, few-shot, and chain-of-thought
- Includes a small synthetic dataset for demos and testing
- Offers a browser-based UI for easy capstone demonstration

## Project Structure
- `app.py` – core logic for interacting with Ollama
- `ui_app.py` – Streamlit web interface
- `data/synthetic_emails.json` – sample emails for testing
- `capstone_report.md` – markdown report aligned to the capstone guidelines
- `requirements.txt` – dependency notes

## Setup
1. Install Ollama from https://ollama.com/
2. Pull a local model, for example:
   - `ollama pull llama3.2:3b`
3. Start the Ollama service:
   - `ollama serve`
4. Install Streamlit:
   - `pip install streamlit`
5. Launch the UI:
   - `streamlit run ui_app.py`

## Demo Commands
- Run the Streamlit app:
  - `streamlit run ui_app.py`
- Run the unit tests:
  - `python -m unittest discover -s tests`

## Capstone Alignment
This project follows the requested capstone guidelines by:
- using only open-source local models
- avoiding proprietary APIs
- documenting prompt strategies
- providing a report with problem statement, dataset source, model comparison, limitations, and future work
