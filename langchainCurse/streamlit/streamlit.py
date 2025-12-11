from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import streamlit as st

chatModel = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

st.set_page_config(page_title="ChatBot basico", page_icon="🤖")
st.title("Chat Fast")
st.markdown("Bienvenido al chatBot  basico Streamlit")