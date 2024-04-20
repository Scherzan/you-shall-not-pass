import streamlit as st
from PIL import Image
#from streamlit_extras.app_logo import add_logo
#from streamlit_extras.colored_header import colored_header

st.set_page_config(
    layout="wide",
)

# This talk is going to be about practices and tools to use while coding mainly 
# to showcase basic security precautions.
# This talk is not design software engineers or security specialists 
# and also not for those who are lucky to work in an environment with scrutinized secure coding system in place.
# The talk will hopefully be enjoyable for you if you love to play around in python and you have come to the conclusion that
# it might be too risky to continue copy pasting all stackoverflow answers directly into your temrinal. 


# Implementing security often feels like a chore especially when we are ecited to see our ideas in action
# Also technology evolves so quickly and usuall we know so little about what software and dependencies we are actually using,
# so following security news and react to the relevant stuff seems cumbersome and hard to do on our own.
# Luckily, you are here, hopefully not because someone broke into your device, and we have some time to dive into tools and practices 
# but first a few words on Roman and myself:

# Roman you want to start?

# Like Roman I am a ml engineer at the same company and we work hard to bring 
# the benefits of ml and functioning technology to public institutions


col1, col2 = st.columns([6,5])

with col1:


    st.write('#')
    st.write('#')
    st.write('#')
    st.markdown('''# You shall not pass! 🧙 Strengthen your python code against attacks.''')


    st.write('#')

    st.markdown('''# Antonia Scherz, Roman Krafft''')
    st.markdown('''### 22.-24.04.2024''')
    st.markdown('''### PyCon DE & PyData Berlin 2024''')

with col2:
    st.write('#')
    #image = Image.open("pages/images/pycon_pydata_logo.png")
    #st.image(image, width = 400)