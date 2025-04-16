import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="LeverFul",  # Título de la ventana en el navegador
    page_icon="",           # Icono vacío
    layout="centered",      # Diseño centrado
    initial_sidebar_state="auto"
)

# --- ESTÉTICA PERSONALIZADA ---
st.markdown(
    """
    <style>
    body {
        background-color: #0e1117;
        color: white;
    }

    .titulo {
        font-size: 48px;
        font-weight: 100;
        color: #D0E7FF;
        text-align: center;
        margin-bottom: 10px;
        font-family: 'Montserrat', sans-serif;
    }

    .subtext {
        text-align: center;
        color: #aaa;
        font-size: 18px;
        margin-bottom: 40px;
    }

    .stButton > button {
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        transition: background-color 0.3s ease;
        border: none;
    }

    .stButton > button:hover {
        background-color: #ff6666;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título de la página
st.markdown('<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@100;300;400&display=swap" rel="stylesheet"> <div class="titulo">LeverFul</div>', unsafe_allow_html=True)

# Subtítulo
st.markdown('<div class="subtext">Bienvenido a la plataforma LeverFul. Esta pagina hay vaias herramientas de IA, cada una esta especializada para su trabajo, para poder utilizarla, debe registrarse y en la zona de API debe insertar su api. Para obtener la API, necesitas registrarte en [AI21 LABS](https://www.ai21.com) e ir a la zona de APIs, ahi estara tu API la cual debes insertar aca.  Selecciona la opción que deseas.</div>', unsafe_allow_html=True)
st.markdown("Aca hay varias IAs. Selecciona la opción que desees:")
# Botones para navegar a otras páginas
if st.button("🧠 IA Principal"):
    st.switch_page("pages/1_IA.py")  # Cambia a la página de IA

if st.button("📑 Resumidor"):
    st.switch_page("pages/2_Resumidor.py")  # Cambia a la página de Resumidor

if st.button("📖 Creador de Historias"):
    st.switch_page("pages/3_Creador de Historias.py")  # Cambia a la página de Creador de Historias
