# Capstone Project Report: Email Reply Assistant

## 1. Problem Statement
The goal of this project is to build an intelligent email reply assistant that can generate concise, professional email responses using a local open-source LLM. The solution demonstrates how AI can assist with communication tasks while keeping inference local and low-cost.

## 2. Dataset Source
The project uses a synthetic dataset stored in `data/synthetic_emails.json`.
- Source type: synthetic/generated data
- Reason: avoids sensitive or confidential information while still allowing testing of real-world email scenarios

## 3. Model Comparison
Two open-source models were considered for local use with Ollama:

| Model | Size | Latency | Accuracy | Cost/Memory | Use Case Fit | Overall Score |
|---|---:|---:|---:|---:|---:|---:|
| Llama 3.2 3B | Medium | Medium | 8.7/10 | 4/5 | Strong | 8.5/10 |
| Phi-3 Mini | Small | Fast | 7.8/10 | 4/5 | Good | 7.9/10 |

### Selection Justification
The final model selected is `llama3.2:3b` because it provided better response quality and stronger instruction-following behavior for professional email writing. Although it is slightly slower than Phi-3 Mini, the difference in quality and clarity makes it a better fit for the use case.

## 4. Prompt Engineering / Optimization
The project tested three strategies:
- Zero-shot prompting
- Few-shot prompting
- Chain-of-thought style prompting

### Observed Results
- Zero-shot was simple and fast.
- Few-shot produced more polished and consistent replies.
- Chain-of-thought prompting improved structure and clarity for more complex messages.

## 5. Demo Results
Example input:
- "Hi Team, I wanted to follow up on the project timeline for the AI assistant demo."

Example output:
- "Hi Team, thank you for the update. I will review the timeline and share any concerns before the presentation."

## 6. Limitations and Future Work
- The current version uses a small synthetic dataset.
- Response quality depends on the local model and hardware.
- Future work can include a web UI, sentiment-aware replies, and multilingual support.

## 7. Documentation of Prompts Used
The prompt templates are implemented in `app.py` and include:
- Zero-shot prompt
- Few-shot prompt with examples
- Chain-of-thought planning prompt
