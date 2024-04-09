
import streamlit as st

col_a, col_b= st.columns(2)

with col_a:
    #st.header("It's me")
    st.write("### This is Me")

    st.write("""
    🏷️: Antonia Scherz \n
    🏠: Berlin \n
    🏢: PD - Berater der öffentlichen Hand \n
    🧭: Senior Specialist/ML Engineer \n
    """)
    #st.image("images/anto_scherz.jpg")
    #st.write("LinekdIn: [https://www.linkedin.com/in/antonia-scherz-7b4740178](%s)" % "https://www.linkedin.com/in/antonia-scherz-7b4740178")
       
with col_b:
    #st.header("It's me")
    st.write("### This is Me again")

    st.write("""
    🏷️: Roman Krafft \n
    🏠: Kaiserslautern \n
    🏢: PD - Berater der öffentlichen Hand \n
    🧭: Senior Specialist/Software Developer \n
    """)
    #st.image("images/roman_krafft.jpg")
    #st.write("LinekdIn: [https://www.linkedin.com/in/antonia-scherz-7b4740178](%s)" % "https://www.linkedin.com/in/antonia-scherz-7b4740178")
