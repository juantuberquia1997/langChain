from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature = 0.7)

ejemplos_sentimientos = [
    HumanMessage(content="Texto a analizar: Me encanta este producto, es increíble"),
    AIMessage(content="POSITIVO"),
    HumanMessage(content="Texto a analizar: El servicio fue terrible, muy decepcionante"),
    AIMessage(content="NEGATIVO"),
    HumanMessage(content="Texto a analizar: El clima está nublado hoy"),
    AIMessage(content="NEUTRO")
]

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un experto en análisis de sentimientos. Clasifica cada texto como: POSITIVO, NEGATIVO o NEUTRO."),
    MessagesPlaceholder(variable_name="ejemplos"),
    ("human", "Texto a analizar: {texto_usuario}")
])

chain = chat_prompt | llm
result=chain.invoke({"ejemplos": ejemplos_sentimientos, "texto_usuario": "hoy mi novia me termino"})
 