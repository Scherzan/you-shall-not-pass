import streamlit as st
from PIL import Image
#from streamlit_extras.app_logo import add_logo
#from streamlit_extras.colored_header import colored_header

st.set_page_config(
    layout="wide",
)



col1, col2 = st.columns([6,5])

with col1:


    st.write('#')
    st.write('#')
    st.write('#')
    st.markdown('''# You Shall Not Pass''')
    st.markdown('''# 🧙''')

    st.write('#')

    st.markdown('''# Antonia Scherz, Roman Krafft''')
    st.markdown('''### 22.-24.04.2024''')
    st.markdown('''### PyCon DE & PyData Berlin 2024''')

with col2:
    st.write('Containes preliminary notes and talk structure as well as ideas what to say to the audience')
    st.write('#')
    st.write('#')
    st.write('#')
    st.write('#')
    st.write('#')
    st.write('#')
    st.write('#')
    #image = Image.open("pages/images/pycon_pydata_logo.png")
    #st.image(image, width = 400)