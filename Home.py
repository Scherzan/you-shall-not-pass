import streamlit as st
from PIL import Image

st.set_page_config(
    layout="wide",
)



col1, col2 = st.columns([6,5])

with col1:


    st.write('#')
    st.write('#')
    st.write('#')
    st.markdown('''# You shall not pass! 🧙 Strengthen your python code against attacks.''')


    st.write('#')
    col1, mid1, mid2, col2 = st.columns((1,0.25,3.5,1))

    with mid1:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.image("./pages/assets/pycon_pydata_logo.png", width = 300)
    with mid2:
        st.markdown('''### Antonia Scherz, Roman Krafft''')
        st.markdown('''#### PyCon DE & PyData Berlin 2024''')
    


with col2:
    st.write('#')
