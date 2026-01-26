from langchain_community.document_loaders import WebBaseLoader

# its useful to do web scraping
 
# Ejemplo básico: cargar documentación
# loader = WebBaseLoader("https://docs.langchain.com/")
# docs = loader.load()
 
# print(f"Título: {docs[0].metadata.get('title', 'Sin título')}")
# print(f"URL: {docs[0].metadata['source']}")
# print(f"Contenido: {docs[0].page_content[:300]}...")
 
# Ejemplo avanzado: múltiples URLs con configuración personalizada
urls = [
   "https://supermu.com/"
]
 
loader = WebBaseLoader(
    web_paths=urls,
    # bs_kwargs=dict(
    #     parse_only=bs4.SoupStrainer(
    #         "div", {"class": ["main-content", "article-content"]}
    #     )
    # )
)
docs = loader.load()

print(f"Páginas_cargadas: {(docs)}")
 
print(f"Páginas cargadas: {len(docs)}")
for i, doc in enumerate(docs):
    print(f"Página {i+1}: {doc.metadata['source']}")
    print(f"Longitud: {len(doc.page_content)} caracteres")