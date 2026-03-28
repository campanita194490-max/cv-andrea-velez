# app_cv.py
import streamlit as st
import os
import glob
import base64

# 📌 Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 📷 Función para cargar imagen como fondo
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# 🔍 Buscar imagen de fondo automáticamente
fondo = glob.glob(os.path.join(BASE_DIR, "fondo.*"))

# 1. Configuración de la página
st.set_page_config(
    page_title="CV - Andrea Vélez",
    page_icon="📄",
    layout="wide"
)

# 🎨 Aplicar fondo si existe
if fondo:
    fondo_base64 = get_base64(fondo[0])
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{fondo_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .main {{
            background-color: rgba(255, 255, 255, 0.85);
            padding: 20px;
            border-radius: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 2. Sidebar con contacto
with st.sidebar:
    imagenes = glob.glob(os.path.join(BASE_DIR, "foto.*"))
    if imagenes:
        st.image(imagenes[0], width=150)
    st.write("📍 **Medellín, Colombia**")
    st.markdown("### 📩 Contacto")
    st.markdown("📧 campanita19449@hotmail.com")
    st.markdown("📧 campanita194490@gmail.com")
    st.markdown("📞 **301 241 1168**")
    st.divider()
    st.write("✨ *Combinando 20 años de experiencia comercial con la potencia de la IA.*")

# 3. Encabezado profesional
st.title("Andrea Vélez Perdomo")
st.subheader("Data Science Trainee | Experta en Gestión Comercial & Ventas")

# 4. Tabs
tab1, tab2, tab3 = st.tabs(["👤 Perfil y Experiencia", "🛠️ Habilidades", "🚀 Proyectos"])

# ---------------- TAB 1 ----------------
with tab1:
    st.header("📝 Resumen Profesional")
    st.write("Profesional con más de 20 años de trayectoria sólida en el área comercial (EFICACIA, EXTRAS). Actualmente cursando Ciencia de Datos e IA en la UdeA, uniendo la experiencia en ventas con el análisis de datos.")
    st.header("💼 Experiencia Laboral")
    st.info("**Asesora Comercial / Soporte | EFICACIA (2017 – 2024)**")
    st.write("- Gestión de bases de datos de clientes y manejo de CRM.")
    st.info("**Asesora Comercial | EXTRAS (2006 – 2014)**")
    st.write("- Liderazgo en ventas y cumplimiento constante de metas comerciales.")

# ---------------- TAB 2 ----------------
with tab2:
    st.header("🛠️ Stack Tecnológico")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Datos e IA**")
        st.code("Python\nPandas\nStreamlit\nSQL\nMachine Learning")
    with col2:
        st.write("**Gestión y Diseño**")
        st.code("Excel Avanzado\nCRM\nPhotoshop\nCiberseguridad")

# ---------------- TAB 3 ----------------
with tab3:
    st.header("🚀 Portafolio de Proyectos")
    st.subheader("1. Dashboard de E-commerce")
    st.write("Análisis interactivo de 5,000 registros de ventas en tiempo real.")
    st.markdown("[Ver Dashboard en Vivo](https://dashboard-ecommerce-andrea-velez.streamlit.app/)")
    
    st.divider()
    
    st.subheader("2. Proyecto de Ciberseguridad")
    st.write("Demostración técnica de protocolos de seguridad y protección de activos digitales.")
    videos = glob.glob(os.path.join(BASE_DIR, "VID*.mp4"))
    if videos:
        st.video(videos[0])
    else:
        st.warning("⚠️ No se encontró video")
    
    st.write("""
    **Lo que logré en este proyecto:**
    - Análisis de vulnerabilidades en sistemas de información.
    - Aplicación de buenas prácticas para la protección de datos sensibles.
    """)
