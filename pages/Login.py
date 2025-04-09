import streamlit as st
from bitstring import BitArray

def Binario(texto):
    
    binario = ' '.join(BitArray(bytes=c.encode()).bin for c in texto)
    
    return binario


st.title("Inicio de sesion")

Base_de_datos = {"Julian": "01010000 01110010 01110101 01100101 01100010 01100001"}

# Entrada de texto
usuario = st.text_input("Escribe tu nombre")
Contraseña = st.text_input("Escribe tu contraseña", type="password")

# Botóns
if st.button("Iniciar sesion"):
    if Binario(Contraseña) == Base_de_datos[usuario]:
        st.write(f"¡Hola, {usuario}!")
        st.session_state["Auntentificado"] = True
        st.session_state["usuario"] = usuario
        st.switch_page("Menu.py")
        
    else: 
        st.write("Contraseña incorrecta")