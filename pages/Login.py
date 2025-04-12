import streamlit as st
from bitstring import BitArray
from peewee import MySQLDatabase, Model, CharField, IntegerField

db = MySQLDatabase(
    'defaultdb',
    user= st.secrets["Usuarios_1"] ,
    password= st.secrets["Password"],
    host=st.secrets["Host"],
    port=19758
)
class Usuario(Model):
    nombre = CharField()
    contraseña = CharField()
    Api = CharField()

    class Meta:
        database = db
def Binario(texto):
    
    binario = ' '.join(BitArray(bytes=c.encode()).bin for c in texto)
    
    return binario


st.title("Inicio de sesion")


# Entrada de texto
usuario = st.text_input("Escribe tu nombre")
Contraseña = st.text_input("Escribe tu contraseña", type="password")

# Botóns
if st.button("Iniciar sesion"):
    db.connect()
    db.create_tables([Usuario])
    User = Usuario.select().where(Usuario.nombre == usuario).first()
    if User == None:
        st.warning("Usuario no encontrado")
    else:
        if Binario(Contraseña) == User.contraseña:
            st.write(f"¡Hola, {usuario}!")
            st.session_state["Auntentificado"] = True
            st.session_state["usuario"] = usuario
            st.session_state["Api"] = User.Api
            st.switch_page("Menu.py")
            
        else: 
            st.warning("Contraseña incorrecta")
