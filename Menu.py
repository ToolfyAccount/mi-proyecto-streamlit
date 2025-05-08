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
    background: radial-gradient(circle at top left, #4C4E6B, #2D3547);  /* Colores morado y azul oscuros */
    color: #fff;
    font-weight: 700;
    font-size: 15px;
    padding: 14px 30px;
    border: none;
    border-radius: 50px;
    box-shadow: inset 0 0 0 0 #fff, 0 8px 20px rgba(0, 0, 0, 0.2);
    cursor: pointer;
    transition: all 0.35s ease;
    position: relative;
    overflow: hidden;
    opacity: 0;
    transform: translateY(30px) scale(0.95);
    animation: enterButton 0.8s ease-out 0.2s forwards;
}

@keyframes enterButton {
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

.stButton > button::before {
    content: "";
    position: absolute;
    top: 50%;
    left: 50%;
    width: 300%;
    height: 300%;
    background: rgba(255, 255, 255, 0.1);
    transition: all 0.75s ease;
    border-radius: 50%;
    transform: translate(-50%, -50%) scale(0);
    z-index: 0;
}

.stButton > button:hover::before {
    transform: translate(-50%, -50%) scale(1);
}

.stButton > button:hover {
    transform: scale(1.08);
    box-shadow: inset 0 0 0 2px #fff, 0 12px 24px rgba(0, 0, 0, 0.25);
}
        .stTextInput > div > div > input {
            background-color: #1e1e2f;
            color: #ffffff;
            border: 2px solid transparent;  /* Sin borde por defecto */
            border-radius: 8px;
            padding: 12px 16px;
            font-size: 16px;
            font-family: 'Arial', sans-serif;
            outline: none;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }

        .stTextInput > div > div > input:focus {
            border: 2px solid transparent;  /* Sin borde al hacer clic */
            background-color: #232342;  /* Cambia el color de fondo cuando está enfocado */
            box-shadow: 0 4px 10px rgba(76, 175, 80, 0.5);  /* Sombras personalizadas */
            transform: scale(1.05);
            color: #f0f0f0;
        }

        .stTextInput > div > div > input:hover {
            background-color: #2b2b45;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
        }

        .stTextInput > div > div > input:focus:hover {
            border: 2px solid transparent;  /* Asegura que no haya borde cuando está enfocado y el mouse encima */
            background-color: #232342;  /* Fondo al estar enfocado */
            box-shadow: 0 4px 10px rgba(76, 175, 80, 0.5);  /* Sombras */
        }

        .stTextInput > div > div > input::placeholder {
            color: #888;
            font-style: italic;
        }

        .stTextInput > div > div > input:focus::placeholder {
            color: #b0c9ff;
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
        st.session_state["Ir"] = "pages/4_LeverFul Cold.py"
        st.switch_page("pages/4_LeverFul Cold.py")
    else:
        st.switch_page("pages/4_LeverFul Cold.py")

# Forzar a Streamlit a usar el puerto que Railway asigna
port = os.environ.get("PORT", 8501)
