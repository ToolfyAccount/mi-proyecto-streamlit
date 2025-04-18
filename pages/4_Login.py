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
    user=os.environ.get("Usuarios_1"),
    password=os.environ.get("Password"),
    host=os.environ.get("Host"),
    port=19758,
    ssl={'fake_flag_to_enable_ssl': True}  # ✅ Este es el cambio importante
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
