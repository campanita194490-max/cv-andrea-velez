import streamlit as st
import os
import glob
import base64

# 📌 Configuración DEBE ir primero
st.set_page_config(
    page_title="CV - Andrea Vélez",
    page_icon="📄",
    layout="wide"
)

# 📌 Ruta base
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 📷 FUNCIÓN PARA CARGAR IMAGEN COMO FONDO
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# 🔍 Buscar imagen de fondo
fondo = glob.glob(os.path.join(BASE_DIR, "fondo.*"))

# 🎨 APLICAR FONDO (más seguro)
if fondo:
    try:
        fondo_base64 = get_base64(fondo[0])

        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpg;base64,{fondo_base64}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except:
        st.warning("⚠️ Error cargando fondo")
else:
    st.warning("⚠️ No se encontró imagen de fondo")

# ---------------- SIDEBAR ----------------
with st.sidebar:

    imagenes = glob.glob(os.path.join(BASE_DIR, "foto.*"))

    if imagenes:
        st.image(imagenes[0], width=150)
    else:
        st.warning("⚠️ No se encontró foto")

    st.write("📍 Medellín, Colombia")

    st.markdown("### 📩 Contacto")
    st.markdown("📧 campanita19449@hotmail.com")
    st.markdown("📧 campanita194490@gmail.com")
    st.markdown("📞 301 241 1168")

    st.divider()
    st.write("✨ 20 años de experiencia + IA")

# ---------------- HEADER ----------------
st.title("Andrea Vélez Perdomo")
st.subheader("Data Science Trainee | Gestión Comercial & Ventas")

# ---------------- TABS ----------------
tab1, tab2, tab3 = st.tabs([
    "👤 Perfil",
    "🛠️ Habilidades",
    "🚀 Proyectos"
])

# ---------------- TAB 1 ----------------
with tab1:
    st.header("📝 Resumen Profesional")
    st.write("""
    Profesional con más de 20 años en el área comercial.
    Actualmente en formación en Ciencia de Datos e IA.
    """)

    st.header("💼 Experiencia")

    st.info("EFICACIA (2017 – 2024)")
    st.write("- Manejo de CRM y bases de datos")

    st.info("EXTRAS (2006 – 2014)")
    st.write("- Cumplimiento de metas comerciales")

# ---------------- TAB 2 ----------------
with tab2:
    st.header("🛠️ Habilidades")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Datos e IA**")
        st.code("Python\nPandas\nStreamlit\nSQL")

    with col2:
        st.write("**Gestión**")
        st.code("Excel\nCRM\nPhotoshop")

# ---------------- TAB 3 ----------------
with tab3:
    st.header("🚀 Proyectos")

    st.subheader("Dashboard E-commerce")
    st.link_button(
        "Ver Dashboard",
        "https://dashboard-ecommerce-andrea-velez.streamlit.app/"
    )

    st.divider()

    st.subheader("Demo en Video")

    # ❌ Quitamos videos pesados
    # ✅ Usamos YouTube (MUY IMPORTANTE para Cloud)
    st.video("https://youtu.be/dA3Kchg_cgA")
