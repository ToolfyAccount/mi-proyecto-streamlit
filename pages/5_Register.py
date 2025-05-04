from peewee import MySQLDatabase, Model, CharField, IntegerField
import streamlit as st
from bitstring import BitArray
import hashlib
import os
from streamlit_cookies_controller import CookieController


cookies = CookieController()


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
    db.connect()
    db.create_tables([Usuario])
    # Verificar si el nombre ya existe
    existe = Usuario.select().where(Usuario.nombre == usuario).exists()
    for u in Usuario.select():
        st.write(f"[DEBUG] Usuario en DB: {u.nombre}")

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
