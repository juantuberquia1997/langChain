
import streamlit as st
from service.pdf_processor import readPdf
from service.cv_evaluator import evaluar_candidato
from ui.components.showResults import mostrar_resultados

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
        
        st.session_state['resultado'] = resultado

        mostrar_resultados(resultado)