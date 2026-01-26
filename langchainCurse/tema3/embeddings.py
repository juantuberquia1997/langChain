from langchain_openai import OpenAIEmbeddings
import numpy as np

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

text1= "La capital de colombia es Bogotá"
text2= "Lima es la capital de Perú"

vec1 = embeddings.embed_query(text1)
vec2 = embeddings.embed_query(text2)

cos_sim = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
print("cos_sim", cos_sim)