import streamlit as st

st.write("### structure of chapter:")
st.write("""
         3. stay informed (tackle info fatigue) + ressources
         how to go about information fatigue : where to find ressources:
         - stay up to date/notifications/information fatigue
         """)

st.write("- cves \n")

#vulnerability notifications - interact with lockfiles
- notification on changes or new versions in dependencies (f.e. new vulnerability discovered)
- Tool PyUp, Dependabot (check on warehouse PyPI  automated pull request notifications)
- usefull because fast notification on compromised packages and speed up upgrade path - merge as soon as new vulnerability is out
- practices run CI  and dependency checks every time  a/this pull request is made no manual update like run pip compile necessary
