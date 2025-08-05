# rag.py

class RAGModel:
    def __init__(self, openai_client):
        self.openai_client = openai_client

    def generate(self, query, results=None):
        prompt = f"Question: {query}\nAnswer:"

        response = self.openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful assistant. "
                        "Be thorough but concise. "
                        "Feel free to ask for clarification if needed."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response
