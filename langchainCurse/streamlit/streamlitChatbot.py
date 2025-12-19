from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import PromptTemplate
import streamlit as st
import copy

st.set_page_config(page_title="ChatBot basico", page_icon="🤖")
st.title("Chat Faster")
st.markdown("Bienvenido al chatBot basico usando Langchain y Streamlit")

temperature = "",
model_name = ""


with st.sidebar:
    st.title("Configuración")
    temperature = st.slider("Temperatura", 0.0, 1.0, 0.5, 0.1)
    model_name = st.selectbox("Modelo", ["gpt-3.5-turbo", "gpt-4", "gpt-4o-mini"])
    if st.button("🗑️ Nueva conversación"):
        st.session_state.messages = []
    chatModel = ChatOpenAI(model=model_name, temperature=temperature)

template = PromptTemplate(
  input_variables=["mensaje", "historial"],
  template=(
    "Eres un asistente útil y amigable llamado ChatBot fast \n\n"  
    "historial de conversacion: {historial} \n\n"
    "Responde de manera clara y concisa a la siguiente pregunta: {mensaje} \n\n"
 ) 
)

chain = template | chatModel

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
question = st.chat_input("Escribe tu pregunta")
if question:
    with st.chat_message("human"):
       st.markdown(question)

    #save message like human message
    st.session_state.messages.append(HumanMessage(content=question))

    # response from assistant
    response = chain.invoke({
      "mensaje": question,
      "historial": st.session_state.messages
    })
    

    #show response in the interface
    with st.chat_message("assistant"):
        st.markdown(response.content)

    st.session_state.messages.append(AIMessage(content=response.content))

