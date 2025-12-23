from langchain_core.runnables import RunnableLambda, RunnableParallel
from langchain_openai import ChatOpenAI
import json
from langchain_core.prompts import PromptTemplate
import streamlit as st
 
 # Configuración del modelo
llm = ChatOpenAI(model="gpt-4o-mini", temperature = 0)

question = st.chat_input("Escribe tu pregunta")

def cleanInputText(text):
  textValidate= len(text.strip())
  if textValidate > 500:
    st.markdown("Texto demasiado largo, limite de 500 caracteres")
  else:
    return text.strip()
  
def createSummary(text):
    prompt= f"Resume en una sola oración de 20 palabras con el siguiente texto: {text}"
    response = llm.invoke(prompt)
    return response.content

def analizeFeeling(text):
    prompt = f"""
    Tu tarea es analizar el sentimiento del texto.

    REGLAS ESTRICTAS (OBLIGATORIAS):
    - Devuelve SOLO un JSON válido.
    - NO agregues texto antes o después.
    - NO uses markdown.
    - NO uses ``` ni etiquetas.
    - NO expliques nada.

    Texto:
    {text}

    Formato EXACTO de salida:
    {{"sentimiento":"positivo|negativo|neutro","razon":"string"}}
    """
    response = llm.invoke(prompt)
  
    try:
       return json.loads(response.content)
    except json.JSONDecodeError:
        return {"sentimiento": "neutro", "razon": "Error en análisis"}
   
if question:
  preprocessor = RunnableLambda(cleanInputText)
  summary = RunnableLambda(createSummary)
  chain = preprocessor | summary 
  resultado = chain.invoke(question)  
  st.markdown(resultado)

  analize = RunnableLambda(analizeFeeling)
  result= analize.invoke(question)
  st.markdown(result)

    
   