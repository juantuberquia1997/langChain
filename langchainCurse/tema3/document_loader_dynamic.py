from langchain_community.document_loaders import SeleniumURLLoader
from selenium.webdriver.chrome.options import Options

# Configurar opciones de navegador, ajustar no funciona
chrome_options = Options()
chrome_options.add_argument("--headless")  # Sin interfaz gráfica
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
 
# URLs con contenido dinámico
urls = [
   "https://supermu.com/"
]
 
loader = SeleniumURLLoader(
    urls=urls,
    # browser="chrome",
    # executable_path="/path/to/chromedriver",  # Opcional si está en PATH
    # chrome_options=chrome_options
)
 
docs = loader.load()
 
for i, doc in enumerate(docs):
  print(f"\n=== PÁGINA {i+1} ===")
  print(f"URL: {doc.metadata['source']}")
  print(f"Contenido renderizado: {(doc)}")
  
  # # Buscar elementos que indiquen contenido dinámico
  # dynamic_indicators = ['data-', 'ng-', 'v-', 'react-', 'vue-']
  # has_dynamic = any(indicator in doc.page_content for indicator in dynamic_indicators)
  # print(f"Contiene elementos dinámicos: {'Sí' if has_dynamic else 'No'}")
    