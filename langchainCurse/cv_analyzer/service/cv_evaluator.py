from langchain_openai import ChatOpenAI
from prompts.cv_prompts import crear_sistema_prompts
from models.cv_models import CV_analyzer


def evaluar_candidato ( texto_cv, descripcion_puesto):
  try:
    chainAnalyzerCV = evaluar_cv()
    result = chainAnalyzerCV.invoke({"texto_cv": texto_cv, "descripcion_puesto": descripcion_puesto})
    return result
  
  except Exception as e:
    return f"Error: No se pudo analizar el currículum:  {str(e)}"

def evaluar_cv():
  llm = ChatOpenAI(model="gpt-4o-mini", temperature = 0.2)

  resultStructure = llm.with_structured_output(CV_analyzer)
  chain = crear_sistema_prompts() | resultStructure

  return chain