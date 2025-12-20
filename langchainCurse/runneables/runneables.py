from langchain_core.runnables import RunnableLambda 

paso1 = RunnableLambda(lambda x: x)

def quarterNumber(x):
  return x**2

paso2 = RunnableLambda(quarterNumber)
chain = paso1 | paso2
result = chain.invoke(4)

print(result)