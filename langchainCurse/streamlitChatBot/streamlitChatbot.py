from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import streamlit as st

st.set_page_config(page_title="ChatBot basico", page_icon="🤖")
st.title("Chat Faster")
st.markdown("Bienvenido al chatBot basico usando Langchain y Streamlit")

temperature = ""
model_name = ""
personalizationSystem = ""

with st.sidebar:
    st.title("Configuración")
    temperature = st.slider("Temperatura", 0.0, 1.0, 0.5, 0.1)
    model_name = st.selectbox("Modelo", ["gpt-3.5-turbo", "gpt-4", "gpt-4o-mini"])
    personalizationSystem = st.selectbox("Personalidad del Agente", ["Útil y amigable", "Experto técnico", "Creativo y divertido"])
    if st.button("🗑️ Nueva conversación"):
        st.session_state.messages = []
    chatModel = ChatOpenAI(model=model_name, temperature=temperature)

chat_prompt = ChatPromptTemplate.from_messages([
  ("system", "Eres un asistente {personalizationSystem} llamado ChatBot fast, responde de manera clara y concisa"),
  MessagesPlaceholder(variable_name="historial"),
  ("human", "{mensaje}"),
])

chain = chat_prompt | chatModel

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

    result= chain.invoke({"mensaje": question, "historial": st.session_state.messages, "personalizationSystem": personalizationSystem})

    print("hsiur", st.session_state.messages)

    #show response in the interface
    with st.chat_message("assistant"):
        st.markdown(result.content)

    st.session_state.messages.append(AIMessage(content=result.content))

