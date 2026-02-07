from langchain_openai import ChatOpenAI
from config.config import QUERY_MODEL

llm = ChatOpenAI(model=QUERY_MODEL, temperature = 0.1)

def setup_llm():

  return llm