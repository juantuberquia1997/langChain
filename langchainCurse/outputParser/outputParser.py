from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from typing import List


llm = ChatOpenAI(model="gpt-4o-mini", temperature = 0.7)

class analyzeText(BaseModel):
    text: str= Field(description="Resumente de los Textos")
    feeling: str = Field(description="califica el Sentimiento de los Texto de 1 a 5, siendo 1 negativo, 5 positivo y 3 neutro")

class AnalyzeResponse(BaseModel):
    results: List[analyzeText]

textInput= "Me encanta salir a conocer nuevos lugares en mi moto, pero me canso la espalda"
textInput2= "No Me encanta salir a conocer nuevos lugares en mi moto, me gusta salir a restaurantes"
resultStructured = llm.with_structured_output(AnalyzeResponse)

result = resultStructured.invoke(f"Analiza los siguientes textos y su feeling respectivamente: {textInput}, {textInput2}")

print("result__", result.model_dump_json())
