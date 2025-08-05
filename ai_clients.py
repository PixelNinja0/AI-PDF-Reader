# ai_clients.py

from openai import OpenAI
import os

# === Echtbetrieb (OpenAI) ===
def get_openai_client():
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# === Dummy-Betrieb ===
class DummyCompletions:
    def create(self, model, messages):
        user_prompt = messages[-1]["content"]
        user_prompt = user_prompt.replace("Question:", "").replace("Answer:", "").strip()

        return type("DummyResponse", (), {
            "choices": [type("Choice", (), {
                "message": type("Message", (), {"content": f"Demo answer for: '{user_prompt}'"})
            })()]
        })

class DummyChat:
    completions = DummyCompletions()

class DummyOpenAIClient:
    chat = DummyChat()

def get_dummy_client():
    return DummyOpenAIClient()
