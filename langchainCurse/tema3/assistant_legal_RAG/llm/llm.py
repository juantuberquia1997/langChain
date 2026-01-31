from langchain_openai import  ChatOpenAI
from prompts.rag_prompts import crear_sistema_prompts
from config.config import QUERY_MODEL, GENERATION_MODEL

llm = ChatOpenAI(model="gpt-4o-mini", temperature = 0.1)

def setup_llm(result_retriever):
  chain = crear_sistema_prompts() | llm

  for i, doc in enumerate(result_retriever):
      summary = chain.invoke({"respuesta_retriever": doc.page_content})
      print(f"similarity_data: {summary.content}")

  # return chain