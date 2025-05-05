import streamlit as st
from streamlit_cookies_controller import CookieController
import os
st.set_page_config(
    page_title="LeverFul",
    page_icon="",
    layout="centered",
    initial_sidebar_state="auto"
)


# Inicializar el controlador de cookies
cookies = CookieController()


if "Guardado" not in st.session_state or not st.session_state["Guardado"]:
    pass

else:
    cookies.set("Username", st.session_state["Guardado"])


Usuario_Logueado = cookies.get("Username")

# Comprobar si el usuario está logueado o no
if Usuario_Logueado is None:
    st.session_state["Auntentificado"] = False
else:
    st.session_state["Auntentificado"] = True
    st.session_state["usuario"] = Usuario_Logueado


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


st.write('''
<div class="subtext">
Bienvenido a la plataforma LeverFul. En esta página encontrarás varias herramientas de IA, cada una especializada en su tarea. Para poder utilizarlas, debes registrarte y automáticamente obtendrás acceso total a las 4 IA's en esta plataforma.

PD:Para mis compañeros de PRAXIS, gracias por usar esta IA, se los agradezco.

Selecciona la opción que deseas.
</div>
''', unsafe_allow_html=True)


st.markdown("Aca hay varias IAs. Selecciona la opción que desees:")

st.write("Para preguntas generales:")

if st.button("🧠 LeverFul AI"):
    if "Auntentificado" not in st.session_state or not st.session_state["Auntentificado"]:
        st.session_state["Ir"] = "pages/1_LeverFul AI.py"
    st.switch_page("pages/1_LeverFul AI.py")
    # Cambia a la página de IA
st.write(" ")
st.write("Para resumir textos o archivos:")

if st.button("📑 LeverFul Snap"):
    if "Auntentificado" not in st.session_state or not st.session_state["Auntentificado"]:
        st.session_state["Ir"] = "pages/2_LeverFul Snap.py"
    # Cambia a la página de Resumidor
    st.switch_page("pages/2_LeverFul Snap.py")

st.write(" ")
st.write("Para crear historias:")


if st.button("📖 LeverFul Maker"):
    if "Auntentificado" not in st.session_state or not st.session_state["Auntentificado"]:
        st.session_state["Ir"] = "pages/3_LeverFul Maker.py"
    st.switch_page("pages/3_LeverFul Maker.py")

st.write(" ")
st.write("Para preguntas generales con respuesta directa")

if st.button("❄️ LeverFul Cold"):
    if "Auntentificado" not in st.session_state or not st.session_state["Auntentificado"]:

    st.switch_page("pages/4_LeverFul Cold.py") 

# Forzar a Streamlit a usar el puerto que Railway asigna
port = os.environ.get("PORT", 8501)
