import streamlit as st
from bitstring import BitArray
from peewee import MySQLDatabase, Model, CharField, IntegerField
import hashlib
import os

def convertir_a_sha256(texto):
    sha256_hash = hashlib.sha256(texto.encode()).hexdigest()
    return sha256_hash

db = MySQLDatabase(
    'defaultdb',
    user=os.environ.get("USUARIOS_1"),    # Lee la variable de entorno USUARIOS_1
    password=os.environ.get("PASSWORD"),   # Lee la variable de entorno PASSWORD
    host=os.environ.get("HOST"),           # Lee la variable de entorno HOST
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
        if convertir_a_sha256(Contraseña) == User.contraseña:
            st.write(f"¡Hola, {usuario}!")
            st.session_state["Auntentificado"] = True
            st.session_state["usuario"] = usuario
            st.session_state["Api"] = User.Api
            st.switch_page("Menu.py")
            
        else: 
            st.warning("Contraseña incorrecta")
