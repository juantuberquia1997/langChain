# una base de datos vectorial almacema el resultado del embedding
# example de una base de datos vectorial opensource son: croma, pinecone 

from langchain_community.document_loaders import PyPDFLoader, PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import os

# load = PyPDFLoader("C:\\Users\\1234\\Documents\\github\\curseIA\\langchainCurse\\tema3\\pdf\\atl_nacional.pdf")
load = PyPDFDirectoryLoader("C:\\Users\\1234\\Documents\\github\\curseIA\\langchainCurse\\tema3\\pdf")
docs= load.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=50)
chunks = text_splitter.split_documents(docs)
embeddings= OpenAIEmbeddings(model="text-embedding-3-large")

vector_store = Chroma.from_documents(
  chunks, 
  embeddings, 
  persist_directory="C:\\Users\\1234\\Documents\\github\\curseIA\\langchainCurse\\tema3\\chromadb" 
)

question = "cuales son los generos musicales ?"

result = vector_store.similarity_search(question, k=3)

for doc in result:
    print(f"similarity_score: {doc.page_content}")