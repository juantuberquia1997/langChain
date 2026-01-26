# una base de datos vectorial almacema el resultado del embedding
# example de una base de datos vectorial opensource son: croma, pinecone 

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import os

load = PyPDFDirectoryLoader("C:\\Users\\1234\\Documents\\github\\curseIA\\langchainCurse\\tema3\\pdf")
docs= load.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=1000)
chunks = text_splitter.split_documents(docs)
embeddings= OpenAIEmbeddings(model="text-embedding-3-large")

vector_store = Chroma.from_documents(
  chunks,
  embeddings, 
  persist_directory="C:\\Users\\1234\\Documents\\github\\curseIA\\langchainCurse\\tema3\\chromadb" 
)

question = "¿dime el nombre de las personas que van a tomar el inmueble?" 
result = vector_store.similarity_search(question, k=2)

for i, doc in enumerate(result):
    print(f"similarity_score: {doc.page_content}")