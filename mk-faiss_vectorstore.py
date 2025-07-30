# mk-faiss_index.py
# (for Windows11 Machine (With GPU) WSL(Ubuntu))

import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Setting
directory_path = "./data"
file_extension = ".md"
db_name = 'vectorstore.db'
embeddings = HuggingFaceEmbeddings(
    model_name = "intfloat/multilingual-e5-large",
    model_kwargs = {'device':'cuda:0'},
)

texts = []
for filename in os.listdir(directory_path):
    if filename.endswith(file_extension):
        file_path = os.path.join(directory_path, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            texts.append(content)

db = FAISS.from_texts(texts, embeddings)
db.save_local(db_name)
