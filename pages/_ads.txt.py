# pages/_ads.txt.py

import streamlit as st

# Oculta el sidebar
st.set_page_config(page_title="ads.txt", layout="wide", initial_sidebar_state="collapsed")

# Establecer tipo de contenido como texto plano
st.markdown(
    '<meta http-equiv="Content-Type" content="text/plain; charset=utf-8"/>',
    unsafe_allow_html=True
)

# Contenido del archivo ads.txt
ads_txt_content = """
google.com, pub-1234567890123456, DIRECT, f08c47fec0942fa0
"""

st.text(ads_txt_content.strip())
