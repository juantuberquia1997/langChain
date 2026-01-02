
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


llm = ChatOpenAI(model="gpt-4o-mini", temperature = 0.7)

chat_prompt = ChatPromptTemplate.from_messages([
  ("human", "{text}"),
  ("system", "you're a translation assistant from spanish to english."),
])

messages = chat_prompt.format_messages(text="hola, soy un desarrollador web y estoy usando langchain")
result= llm.invoke(messages)

print(result.content)