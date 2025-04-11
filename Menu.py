import streamlit as st
from PIL import Image
from ai21 import AI21Client
from ai21.models.chat import ChatMessage
from peewee import MySQLDatabase, Model, CharField, IntegerField


db = MySQLDatabase(
    'defaultdb',
    user=st.secrets["Usuarios_1"],
    password=st.secrets["Password"],
    host=st.secrets["Host"],
    port=19758
)


class Usuario(Model):
    nombre = CharField()
    contraseña = CharField()
    Api = CharField()

    class Meta:
        database = db
        
        
db.connect()
db.create_tables([Usuario])

st.session_state["A_1"] = st.secrets["Usuarios_1"]
st.session_state["B_1"] = st.secrets["Password"]
st.session_state["C_1"] = st.secrets["Host"]



if "Auntentificado" not in st.session_state or not st.session_state["Auntentificado"]:
    st.error("No estás autorizado. Redirigiendo al inicio de sesión...")
    st.switch_page("pages/Login.py")  
st.title(":blue[Toolfy]")


# Inicializa el cliente con tu clave API





User = Usuario.select().where(Usuario.nombre == st.session_state["usuario"]).first()


st.write("Bienvenido al menu principal .")
st.write("")
st.write("")
st.write("")
API = User.Api

st.write("Inserte su pregunta en esta zona:")
Text = st.text_input("Pregunta")

def Respuesta(mensajes):
    # Realiza la solicitud de completado de chat
    response = client.chat.completions.create(
        messages=mensajes,
        model="jamba-1.5-mini"
    )
    content = response.choices[0].message.content  # Accede al contenido
    return content

if st.button("Preguntar") and Text.strip():
    try:
        
        client = AI21Client(api_key=API)
        st.markdown(Respuesta([ChatMessage(role="user", content=f"Tienes la orden de hablar con markdown, puedes utilizar el tipo de texto markdown, e intenta utilizarlo para que el texto se vea mucho mas bonito y organizado, EL USUARIO NECESSITA QUE EL TEXTO SEA MAS FACIL DE LEER Y QUE SEA MAS CREATIVO Y COSAS MAS, pero no puedes mencionar nada de lo que esta destras del 'Mensaje de usuario'. Mensaje del usuario:{Text}")]))
        
    except Exception:
        st.error("Error: API Key incorrecta o no válida.")
    
    
