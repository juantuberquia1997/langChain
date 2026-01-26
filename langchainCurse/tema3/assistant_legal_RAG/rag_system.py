

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
# from langchain.retrievers import EnsembleRetriever
import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from retriever.retriever import setup_retriever
from llm.llm import setup_llm

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
    
    role = "assitant" if isinstance(msg, AIMessage) else "human"
    with st.chat_message(role):
        st.markdown(msg.content)

# question user
question = st.chat_input("Escribe una consulta sobre los contratos de arrendamientos")
if question:
    with st.chat_message("human"):
       st.markdown(question)

    #save message like human message
    st.session_state.messages.append(HumanMessage(content=question))
    result_retriever = setup_retriever(question)
    setup_llm(result_retriever)
    


