from peewee import MySQLDatabase, Model, CharField, IntegerField
import streamlit as st
from bitstring import BitArray
# Conexión a tu base en Aiven
db = MySQLDatabase(
    'defaultdb',
    user=Usuarios_1 ,
    password=Password,
    host=Host,
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



st.title("Registre su cuenta")

st.write("Inserte su API, para conseguir la API, cree una cuenta en [AI21 LABS](https://www.ai21.com), despues vaya a API key, genere su API, y insertela adelante:")
# Entrada de texto
usuario = st.text_input("Escribe tu nombre")
Contraseña = st.text_input("Escribe tu contraseña", type="password")
api = st.text_input("Escribe tu api", type="password")

if st.button("Registrarse"):
    db.connect()
    db.create_tables([Usuario])
    # Verificar si el nombre ya existe
    existe = Usuario.select().where(Usuario.nombre == usuario).exists()
    for u in Usuario.select():
        st.write(f"[DEBUG] Usuario en DB: {u.nombre}")


    if not existe:
        Usuario.create(nombre=usuario, contraseña=Binario(Contraseña), Api=api)
        st.write(f"¡Hola, {usuario}!")
        st.session_state["Auntentificado"] = True
        st.session_state["usuario"] = usuario
        st.switch_page("Menu.py")
    else:
        st.write("El usuario ya está tomado")
        
    db.close()




        
        
        



