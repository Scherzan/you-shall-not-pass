
import streamlit as st

st.set_page_config(
    layout="wide",
)
st.markdown(" ### Feel free to connect and share your thoughts.")
st.markdown("#")
st.markdown("#")

cola, colb, mid, colc, cold = st.columns((4,4,1,4,4))

with cola:
    st.write("### Anto")

    colx, colz = st.columns((1,10))
    with colx:
        st.write("🏷️ ")
        st.write("🏠 ")
        st.write("🧭 ") 
        st.write("🏢 ")
        st.image("./pages/assets/LI-In-Bug.png", width=22)
        
    with colz:
        st.write("Antonia Scherz")
        st.write("Berlin")
        st.write("ML Engineer")
        st.image("./pages/assets/pd.svg", width=28)
        st.write("[https://www.linkedin.com/in/antonia-scherz-7b4740178](%s)" % "https://www.linkedin.com/in/antonia-scherz-7b4740178")
        
with colb:
    st.markdown("#")
    st.image("./pages/assets/anto_scherz.jpeg")


with colc:
    st.write("### Roman")

    colx, colz = st.columns((1,15))
    with colx:
        st.write("🏷️ ")
        st.write("🏠 ")
        st.write("🧭 ") 
        st.write("🏢 ")
        st.image("./pages/assets/LI-In-Bug.png", width=22)
        
    with colz:
        st.write("Roman Krafft")
        st.write("Kaiserslautern")
        st.write("Senior Specialist/Software Developer")
        st.image("./pages/assets/pd.svg", width=28)
        st.write("[https://www.linkedin.com/in/roman-krafft-1b034620b/](%s)" % "https://www.linkedin.com/in/roman-krafft-1b034620b/")

with cold:
    st.markdown("#")
    st.image("./pages/assets/roman_krafft.jpg", width=175)

st.markdown("#")
st.markdown("#")
st.markdown("#")
st.markdown("#")
colx, colz = st.columns((1,25))
with colx:
    st.image("./pages/assets/git_icon.png", width=50)

with colz:
    st.write("")
    st.write("[https://www.linkedin.com/in/roman-krafft-1b034620b/](%s)" % "https://www.linkedin.com/in/roman-krafft-1b034620b/")


