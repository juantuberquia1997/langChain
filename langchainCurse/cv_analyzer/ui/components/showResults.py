import streamlit as st
from models.cv_models import CV_analyzer

def mostrar_resultados(resultado: CV_analyzer):
    """Muestra los resultados del análisis de manera estructurada y profesional"""
    
    st.subheader("🎯 Evaluación Principal")
    
    if resultado.percentaje >= 80:
        color = "🟢"
        nivel = "EXCELENTE"
        mensaje = "Candidato altamente recomendado"
    elif resultado.percentaje >= 60:
        color = "🟡"
        nivel = "BUENO"
        mensaje = "Candidato recomendado con reservas"
    elif resultado.percentaje >= 40:
        color = "🟠"
        nivel = "REGULAR"
        mensaje = "Candidato requiere evaluación adicional"
    else:
        color = "🔴"
        nivel = "BAJO"
        mensaje = "Candidato no recomendado"
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.metric(
            label="Porcentaje de Ajuste al Puesto",
            value=f"{resultado.percentaje}%",
            delta=f"{color} {nivel}"
        )
        st.markdown(f"**{mensaje}**")
    
    st.divider()
    
    st.subheader("👤 Perfil del Candidato")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**👨‍💼 Nombre:** {resultado.name}")
        st.info(f"**⏱️ Experiencia:** {resultado.time_experience} años")
    
    with col2:
        st.info(f"**🎓 Educación:** {resultado.education}")
    
    st.subheader("💼 Experiencia Relevante")
    st.info(f"📋 **Resumen de experiencia:**\n\n{resultado.experience_relevant}")
    
    st.divider()
    
    st.subheader("🛠️ Habilidades Técnicas Clave")
    # if resultado.habilidades_clave:
    #     cols = st.columns(min(len(resultado.habilidades_clave), 4))
    #     for i, habilidad in enumerate(resultado.habilidades_clave):
    #         with cols[i % 4]:
    #             st.success(f"✅ {habilidad}")
    # else:
    #     st.warning("No se identificaron habilidades técnicas específicas")
    
    st.divider()
    
    col_fortalezas, col_mejoras = st.columns(2)
    
    with col_fortalezas:
        st.subheader("💪 Fortalezas Principales")
        if resultado.strengths:
            for i, fortaleza in enumerate(resultado.strengths, 1):
                st.markdown(f"**{i}.** {fortaleza}")
        else:
            st.info("No se identificaron fortalezas específicas")
    
    with col_mejoras:
        st.subheader("📈 Áreas de Desarrollo")
        if resultado.toImprove:
            for i, area in enumerate(resultado.weaknesses, 1):
                st.markdown(f"**{i}.** {area}")
        else:
            st.info("No se identificaron áreas de mejora específicas")
    
    st.divider()
    
    st.subheader("📋 Recomendación Final")
    
    if resultado.percentaje >= 70:
        st.success("""
        ✅ **CANDIDATO RECOMENDADO**
        
        El perfil del candidato está bien alineado con los requisitos del puesto. 
        Se recomienda proceder con las siguientes etapas del proceso de selección.
        """)
    elif resultado.percentaje >= 50:
        st.warning("""
        ⚠️ **CANDIDATO CON POTENCIAL**
        
        El candidato muestra potencial pero requiere evaluación adicional. 
        Se recomienda una entrevista técnica para validar competencias específicas.
        """)
    else:
        st.error("""
        ❌ **CANDIDATO NO RECOMENDADO**
        
        El perfil no se alinea suficientemente con los requisitos del puesto. 
        Se recomienda continuar la búsqueda de candidatos más adecuados.
        """)
    
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("💾 Guardar Análisis", use_container_width=True):
            st.info("Funcionalidad de guardado - En desarrollo")