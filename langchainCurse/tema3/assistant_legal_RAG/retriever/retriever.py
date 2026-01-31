from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from config.config import EMBEDDING_MODEL, CHROMA_DB_PATH, SEARCH_TYPE, MMR_DIVERSITY, MMR_FETCH_K

# retriever tipo MMR

def setup_retriever(question):
  vector_store = Chroma(
    embedding_function = OpenAIEmbeddings(model=EMBEDDING_MODEL),
    persist_directory= CHROMA_DB_PATH 
  )

  retriever = vector_store.as_retriever(search_type=SEARCH_TYPE, search_kwargs=
  {"k": 3, "diversity": MMR_DIVERSITY, "fetch_k": MMR_FETCH_K})

  result= retriever.invoke(question)
  return result
  
