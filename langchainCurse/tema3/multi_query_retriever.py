# uso de multi query retriever para  hacer una consulta mas avanzada de la informacion en una base de datos vectorial
# el llm lo que hace es crear varias preguntas simlares a la pregunta original

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain_classic.retrievers.multi_query import MultiQueryRetriever

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

vector_store = Chroma(
  embedding_function = OpenAIEmbeddings(model="text-embedding-3-large"), 
  persist_directory= "C:\\Users\\1234\\Documents\\github\\curseIA\\langchainCurse\\tema3\\chromadb" 
)

base_retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 2})
retriever = MultiQueryRetriever.from_llm(llm=llm, retriever=base_retriever)

question = "¿cual es la copa mas importante que ha ganado Atletico nacional?" 
result = retriever.invoke(question)

print("result__", result)

for i, doc in enumerate(result):
    print(f"similarity_data: {doc.page_content}")