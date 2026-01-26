from langchain_core.prompts import  SystemMessagePromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate

SISTEMA_PROMPT = SystemMessagePromptTemplate.from_template(
    """Eres un experto analizador de archivos, con 10 años de experiencia en busqueda inteligente en documentos de relacionados con contratos de arrendamientos. 
    Tu especialidad es analizar estos documentos minuciosamente, proporcionando un análisis detallado y objetivo.

    CRITERIOS DE EVALUACIÓN:
    - Coherencia y cohesión en la información
    - Claridad en la información
    - Precisións en la información
    - Consistencia en la información
    - Relevancia en la información
    - Cualidad en la información
    - Eficiencia  en la información     

    """
)

# Prompt de análisis - Instrucciones específicas para evaluar el CV
ANALISIS_PROMPT = HumanMessagePromptTemplate.from_template(
    """Analiza el siguiente contrato de arrendamiento y  responde segun la consulta realizado por el usuario.
    Proporciona un resumen detallado.

**Informacion proveia por la consulta a la base de datos vectorial:**
{respuesta_retriever}

**INSTRUCCIONES ESPECÍFICAS:**
1. Extrae información clave de los documentos de arrendamientos
2. Realiza un resument de la infromación extraída


Sé preciso, objetivo y constructivo en tu análisis."""
)

# Prompt completo combinado - Listo para usar
CHAT_PROMPT = ChatPromptTemplate.from_messages([
    SISTEMA_PROMPT, 
    ANALISIS_PROMPT
])

def crear_sistema_prompts():
    """Crea el sistema de prompts especializado para análisis de documentos de arrendamientos"""
    return CHAT_PROMPT