# server.py

import sys
import os
sys.path.append(os.path.dirname(__file__))

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from rag import RAGModel
from tts import speak
from ai_clients import get_dummy_client, get_openai_client

from dotenv import load_dotenv
load_dotenv()

# Umschalten hier: DUMMY = True oder False
DUMMY = True

# Auswahl des AI-Clients
openai_client = get_dummy_client() if DUMMY else get_openai_client()
rag_model = RAGModel(openai_client=openai_client)

# FastAPI Setup
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/query", response_class=HTMLResponse)
async def query(request: Request):
    form = await request.form()
    user_query = form.get("query")

    response = rag_model.generate(user_query)
    answer = response.choices[0].message.content

    speak(answer)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "question": user_query,
        "answer": answer
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8011)

