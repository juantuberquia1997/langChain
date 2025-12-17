from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import streamlit as st

chatModel = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

st.set_page_config(page_title="ChatBot basico", page_icon="🤖")
st.title("Chat Faster")
st.markdown("Bienvenido al chatBot basico usando Langchain y Streamlit")

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

# # question user
question = st.chat_input("Escribe tu pregunta")
if question:
    with st.chat_message("human"):
       st.markdown(question)

    #save message like human message
    st.session_state.messages.append(HumanMessage(content=question))

    # response from assistant
    response = chatModel.invoke(st.session_state.messages)

    #show response in the interface
    with st.chat_message("assistant"):
        st.markdown(response.content)

    st.session_state.messages.append(AIMessage(content=response.content))