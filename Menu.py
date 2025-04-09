import streamlit as st
from PIL import Image



def Buscar(Texto):
    return f"https://www.google.com/search?q={Texto.replace(' ', '+')}"


if "Auntentificado" not in st.session_state or not st.session_state["Auntentificado"]:
    st.error("No estás autorizado. Redirigiendo al inicio de sesión...")
    st.switch_page("pages/Login.py")  
st.title(":blue[Toolfy]")


st.write("Bienvenido al menu principal .")
st.write("")
st.write("")
st.write("")
st.write('''''')
Text = st.text_input("Buscar")

if st.button("Buscar") and Text.strip():
    st.experimental_open_url(Buscar(Text))
    
    