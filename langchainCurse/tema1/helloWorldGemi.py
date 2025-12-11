from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

question = "What is the most interesting of Medellin?, please response in spanish"
response = llm.invoke(question)
print(response.content)