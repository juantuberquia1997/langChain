# uso de retrievers para recuperar informacion de una base de datos vectorial
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

vector_store = Chroma(
  embedding_function = OpenAIEmbeddings(model="text-embedding-3-large"), 
  persist_directory= "C:\\Users\\1234\\Documents\\github\\curseIA\\langchainCurse\\tema3\\chromadb" 
)

retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 2})
question = "¿dime el nombre de las personas que van a tomar el inmueble?" 
result = retriever.invoke(question)

print("result__", result)

for i, doc in enumerate(result):
    print(f"similarity_data: {doc.page_content}")