import os
import json
from langchain_core.documents import Document
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

with open('datasets/rag_data_metadata.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

split_docs = []

for question, answers in json_data.items():
    answers_str = "\n".join(answers)
    split_docs.append(Document(page_content=question, metadata={"detail":answers_str}))

embedding_model=HuggingFaceEmbeddings(model_name="BAAI/bge-small-zh-v1.5")

vectordb = Chroma.from_documents(documents=split_docs, embedding=embedding_model,
                                     persist_directory='datasets/rag_chroma_db')