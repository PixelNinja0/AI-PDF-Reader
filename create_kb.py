# create_kb.py

import os
import time
from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance, PointStruct
from sentence_transformers import SentenceTransformer
from PyPDF2 import PdfReader
import nltk

nltk.download("punkt")

qdrant_client = QdrantClient(host="localhost", port=6333)
collection_name = "text_collection"

embedder = SentenceTransformer("all-MiniLM-L6-v2")

if qdrant_client.collection_exists(collection_name):
    qdrant_client.delete_collection(collection_name)
    time.sleep(2)

qdrant_client.recreate_collection(
    collection_name=collection_name,
    vectors_config=VectorParams(size=384, distance=Distance.COSINE)
)

def read_pdf_file(file_path):
    text = ""
    with open(file_path, "rb") as file:
        pdf = PdfReader(file)
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def chunk_text(text):
    return nltk.tokenize.sent_tokenize(text)

qdrant_points = []
point_id = 0

for root, dirs, files in os.walk("docs/"):
    for file_name in files:
        if file_name.endswith(".pdf"):
            file_path = os.path.join(root, file_name)
            text = read_pdf_file(file_path)
            chunks = chunk_text(text)
            for idx, chunk in enumerate(chunks):
                embedding = embedder.encode(chunk).tolist()
                qdrant_points.append(
                    PointStruct(id=point_id, vector=embedding, payload={'content': chunk, "file": file_name, "chunk_idx": idx})
                )
                point_id += 1

qdrant_client.upsert(collection_name, qdrant_points)
print(f"Gespeichert {point_id} Textabschnitte aus PDFs.")
