import streamlit as st
from fastapi import FastAPI
from starlette.responses import Response
from streamlit.web.server import Server



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


st.write('''
<div class="subtext">
Bienvenido a la plataforma LeverFul. En esta página encontrarás varias herramientas de IA, cada una especializada en su tarea. Para poder utilizarlas, debes registrarte y, en la zona de API, insertar tu clave API.


Para obtenerla, necesitas registrarte en <a href="https://www.ai21.com" target="_blank">AI21 LABS</a> e ir a la sección de APIs. Allí encontrarás tu API key, la cual deberás insertar aquí. 

Selecciona la opción que deseas.
</div>
''', unsafe_allow_html=True)


st.markdown("Aca hay varias IAs. Selecciona la opción que desees:")
# Botones para navegar a otras páginas
if st.button("🧠 IA Principal"):
    st.switch_page("pages/1_IA.py")  # Cambia a la página de IA

if st.button("📑 Resumidor"):
    st.switch_page("pages/2_Resumidor.py")  # Cambia a la página de Resumidor

if st.button("📖 Creador de Historias"):
    st.switch_page("pages/3_Creador de Historias.py")  # Cambia a la página de Creador de Historias



import os

# Forzar a Streamlit a usar el puerto que Railway asigna
port = os.environ.get("PORT", 8501)


