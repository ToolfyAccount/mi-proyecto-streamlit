from peewee import MySQLDatabase, Model, CharField, IntegerField
import streamlit as st
from bitstring import BitArray
import hashlib
import os
from streamlit_cookies_controller import CookieController


st.set_page_config(

    layout="centered",
    initial_sidebar_state="collapsed"
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
cookies = CookieController()

cookies = CookieController()
Usuario_Logueado = cookies.get("Username")

# Comprobar si el usuario está logueado o no
if Usuario_Logueado is None:
    st.session_state["Auntentificado"] = False
else:
    st.session_state["Auntentificado"] = True
    st.session_state["usuario"] = Usuario_Logueado


def convertir_a_sha256(texto):
    sha256_hash = hashlib.sha256(texto.encode()).hexdigest()
    return sha256_hash


# Conexión a tu base en Aiven
db = MySQLDatabase(
    'defaultdb',
    user=os.environ.get("Usuarios_1"),
    password=os.environ.get("Password"),
    host=os.environ.get("Host"),
    port=19758,
    ssl={'fake_flag_to_enable_ssl': True}  # ✅ Este es el cambio importante
)


class Usuario(Model):
    nombre = CharField()
    contraseña = CharField()

    class Meta:
        database = db


def Binario(texto):

    binario = ' '.join(BitArray(bytes=c.encode()).bin for c in texto)

    return binario


st.title("Registre su cuenta")


# Entrada de texto
usuario = st.text_input("Escribe tu nombre")
Contraseña = st.text_input("Escribe tu contraseña", type="password")


if st.button("Registrarse"):

    if usuario == "":
        st.warning("Escribe un nombre de usuario valido")

    else:
        if Contraseña == "":
            st.warning("Escribe una contraseña valida")

        else:
            db.connect()
            db.create_tables([Usuario])
            # Verificar si el nombre ya existe
            existe = Usuario.select().where(Usuario.nombre == usuario).exists()

            if not existe:
                Usuario.create(
                    nombre=usuario, contraseña=convertir_a_sha256(Contraseña))
                st.write(f"¡Hola, {usuario}!")
                st.session_state["Auntentificado"] = True
                st.session_state["usuario"] = usuario

                cookies.set("Username", usuario)
                st.session_state["Guardado"] = cookies.get("Username")
                st.switch_page("Menu.py")
            else:
                st.write("El usuario ya está tomado")

        db.close()


if st.button("Login"):
    st.switch_page("pages/5_Login.py")
