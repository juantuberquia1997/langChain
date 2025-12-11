from langchain_openai import ChatOpenAI

llm = ChatOpenAI( model="gpt-4o-mini", temperature=0.7)

question = "What is the most interesting of Medellin?, please responde in spanish"
response = llm.invoke(question)
print(response.content)