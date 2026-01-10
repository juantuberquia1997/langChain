import streamlit as st
from service.pdf_processor import readPdf
from service.cv_evaluator import evaluar_candidato
from components.showResults import mostrar_resultados

def main():
    """Función principal que define la interfaz de usuario de Streamlit"""
    
    st.set_page_config(
        page_title="Sistema de Evaluación de CVs",
        page_icon="📄",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.title("📄 Sistema de Evaluación de CVs con IA")
    st.markdown("""
    **Analiza currículums y evalúa candidatos de manera objetiva usando IA**
    
    Este sistema utiliza inteligencia artificial para:
    - Extraer información clave de currículums en PDF
    - Analizar la experiencia y habilidades del candidato
    - Evaluar el ajuste al puesto específico
    - Proporcionar recomendaciones objetivas de contratación
    """)
    
    st.divider()
    
    col_entrada, col_resultado = st.columns([1, 1], gap="large")
    
    with col_entrada:
        procesar_entrada()
    
    with col_resultado:
        mostrar_area_resultados()

def procesar_entrada():
    """Maneja la entrada de datos del usuario"""
    
    st.header("📋 Datos de Entrada")
    
    archivo_cv = st.file_uploader(
        "**1. Sube el CV del candidato (PDF)**",
        type=['pdf'],
        help="Selecciona un archivo PDF que contenga el currículum a evaluar. Asegúrate de que el texto sea legible y no esté en formato de imagen."
    )
    
    if archivo_cv is not None:
        st.success(f"✅ Archivo cargado: {archivo_cv.name}")
        st.info(f"📊 Tamaño: {archivo_cv.size:,} bytes")
    
    st.markdown("---")
    
    st.markdown("**2. Descripción del puesto de trabajo**")
    descripcion_puesto = st.text_area(
        "Detalla los requisitos, responsabilidades y habilidades necesarias:",
        height=250,
        placeholder="""Ejemplo detallado:

**Puesto:** Desarrollador Frontend Senior

**Requisitos obligatorios:**
- 3+ años de experiencia en desarrollo frontend
- Dominio de React.js y JavaScript/TypeScript
- Experiencia con HTML5, CSS3 y frameworks CSS (Bootstrap, Tailwind)
- Conocimiento de herramientas de build (Webpack, Vite)

**Requisitos deseables:**
- Experiencia con Next.js o similares
- Conocimientos de testing (Jest, Cypress)
- Familiaridad con metodologías ágiles
- Inglés intermedio-avanzado

**Responsabilidades:**
- Desarrollo de interfaces de usuario responsivas
- Colaboración con equipos de diseño y backend
- Optimización de rendimiento de aplicaciones web
- Mantenimiento de código legacy""",
        help="Sé específico sobre requisitos técnicos, experiencia requerida y responsabilidades del puesto."
    )
    
    st.markdown("---")
    
    col_btn1, col_btn2 = st.columns([1, 1])
    
    with col_btn1:
        analizar = st.button(
            "🔍 Analizar Candidato", 
            type="primary",
            use_container_width=True
        )
    
    with col_btn2:
        if st.button("🗑️ Limpiar", use_container_width=True):
            st.rerun()
    
    st.session_state['archivo_cv'] = archivo_cv
    st.session_state['descripcion_puesto'] = descripcion_puesto
    st.session_state['analizar'] = analizar

def mostrar_area_resultados():
    """Muestra el área de resultados del análisis"""
    
    st.header("📊 Resultado del Análisis")
    
    if st.session_state.get('analizar', False):
        archivo_cv = st.session_state.get('archivo_cv')
        descripcion_puesto = st.session_state.get('descripcion_puesto', '').strip()
        
        if archivo_cv is None:
            st.error("⚠️ Por favor sube un archivo PDF con el currículum")
            return
            
        if not descripcion_puesto:
            st.error("⚠️ Por favor proporciona una descripción detallada del puesto")
            return
        
        procesar_analisis(archivo_cv, descripcion_puesto)
    else:
        st.info("""
        👆 **Instrucciones:**
        
        1. Sube un CV en formato PDF en la columna izquierda
        2. Describe detalladamente el puesto de trabajo
        3. Haz clic en "Analizar Candidato"
        4. Aquí aparecerá el análisis completo del candidato
        
        **Consejos para mejores resultados:**
        - Usa CVs con texto seleccionable (no imágenes escaneadas)
        - Sé específico en la descripción del puesto
        - Incluye tanto requisitos obligatorios como deseables
        """)

def procesar_analisis(archivo_cv, descripcion_puesto):
    
    """Procesa el análisis completo del CV"""
    
    with st.spinner("🔄 Procesando currículum..."):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.text("📄 Extrayendo texto del PDF...")
        progress_bar.progress(25)
        
        texto_cv = readPdf(archivo_cv)
        
        if texto_cv.startswith("Error"):
            st.error(f"❌ {texto_cv}")
            return
        
        status_text.text("🤖 Preparando análisis con IA...")
        progress_bar.progress(50)
        
        status_text.text("📊 Analizando candidato...")
        progress_bar.progress(75)
        
        resultado = evaluar_candidato(texto_cv, descripcion_puesto)
        
        status_text.text("✅ Análisis completado")
        progress_bar.progress(100)
        
        progress_bar.empty()
        status_text.empty()
        
        mostrar_resultados(resultado)
