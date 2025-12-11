from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

chat = ChatOpenAI( model="gpt-4o-mini", temperature=0.7)

template = PromptTemplate(
  input_variables=["nombre", "ciudad"],
  template=(
    "el nombre del usuario es: {nombre} \n"
    "El usuario es de la ciudad de  {ciudad} \n\n"
    "¿cual es el apellido de la persona que esta hablando? \n"
 ) 
)

chain = template | chat

resultado = chain.invoke(
  {
    "nombre": "Juan",
    "ciudad": "Medellin"
   })

print(resultado.content)