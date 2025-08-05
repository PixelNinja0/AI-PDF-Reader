# 🧠 AI-Powered PDF Reader for the Visually Impaired

An accessible, voice-assisted PDF reader powered by AI – designed to help blind and visually impaired users interact with PDF content using natural language. Developed as a university group project, this tool provides simple question-answer functionality with optional text-to-speech output and a clean web interface.

---

## 🏫 University Project Overview

- Degree Program: Engineering Psychology (B.Sc.)
- Team Size: 6 members  
  - 3 × Concept & UX  
  - 3 × Programming
- My Role: **Team Lead & Fullstack Developer**
- Timeline: Summer Semester 2025
- Goal: Enable barrier-free access to document content using AI

---

## Key Features

- Ask natural-language questions about a PDF file
- Dummy mode for testing without OpenAI API key
- Optional local text-to-speech output (using `pyttsx3`)
- Simple browser-based interface (HTML, CSS, JS)
- Backend powered by FastAPI (Python)

---

## Tech Stack

| Area             | Technologies                  |
|------------------|-------------------------------|
| Backend          | Python · FastAPI              |
| Frontend         | HTML · CSS · JavaScript       |
| AI Integration   | OpenAI (GPT models)           |
| Voice Output     | pyttsx3 (local TTS)           |
| Templates        | Jinja2                        |
| Environment Vars | dotenv                        |

---

## Test Mode: Dummy Client

To avoid API usage during testing, this project includes a **Dummy Mode** that generates simulated answers based on the user’s query. No internet or API key required.

Example:
```txt
Question: What is this PDF about?
→ Demo answer for: 'What is this PDF about?'
