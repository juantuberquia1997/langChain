from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def setup_retriever(question):
  vector_store = Chroma(
    embedding_function = OpenAIEmbeddings(model="text-embedding-3-large"), 
    persist_directory= "C:\\Users\\1234\\Documents\\github\\curseIA\\langchainCurse\\tema3\\chromadb" 
  )

  retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 1})
  result= retriever.invoke(question)
  return result
  
