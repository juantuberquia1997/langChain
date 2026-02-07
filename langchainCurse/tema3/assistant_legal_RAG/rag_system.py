

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
# from langchain.retrievers import EnsembleRetriever
import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
# from retriever.retriever import setup_retriever
from llm.llm import setup_llm
# 
from config.config import EMBEDDING_MODEL, CHROMA_DB_PATH, SEARCH_TYPE, MMR_DIVERSITY, MMR_FETCH_K, QUERY_MODEL
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from prompts.rag_prompts import MULTI_QUERY_PROMPT
# 

# retriever tipo MMR
vector_store = Chroma(
    embedding_function = OpenAIEmbeddings(model=EMBEDDING_MODEL),
    persist_directory= CHROMA_DB_PATH )

base_retriever= vector_store.as_retriever(search_type=SEARCH_TYPE, search_kwargs=
  {"k": 3, "diversity": MMR_DIVERSITY, "fetch_k": MMR_FETCH_K})

retriever = MultiQueryRetriever.from_llm(llm=setup_llm(), retriever=base_retriever, prompt=MULTI_QUERY_PROMPT)

st.set_page_config(page_title="Asistente RAG", page_icon="🤖")
st.title("Asistente RAG")
st.markdown("Sistema de RAG - Asistente legal")

# initial message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# show previous messages
for msg in st.session_state.messages:
    if isinstance(msg, SystemMessage):
        continue
    
    role = "assistant" if isinstance(msg, AIMessage) else "human"
    with st.chat_message(role):
        st.markdown(msg.content)

# question user
question = st.chat_input("Escribe una consulta sobre los contratos de arrendamientos")
if question:
    with st.chat_message("human"):
       st.markdown(question)

    #save message like human message
    st.session_state.messages.append(HumanMessage(content=question))
    result= retriever.invoke(question)
    print(f"Documentos recuperados: {len(result)}")

    


