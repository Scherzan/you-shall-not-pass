import streamlit as st


tab0, tab1, tab2, tab3, tab4  = st.tabs(["coding practices","package management", "code scan", "pypi and open source", "stay informed"])

with tab0:
    st.write("""
             Applying software basics to coding ? Because it is softwarte. \n

             1. update your software (manage dependencies)
             2. use antivirus software (scan your code)
             3. new* stay informed (design smart notification system)
             additions when publishing, \n
             additions web apps (go into less deep) \n
        """)
    

with tab1: # integrate"lockfiles", "hashes", "dependency trees"
   st.write("### structure of chapter:")
   st.write("""
        proper package management:
         important to look for:
         - lockfiles
         - hashes stored (go through in moment)
         - store dependency trees
    """) # word on python updates -> important too.
   st.write("visualisation/display content on each of those")
   

with tab2:
   st.write(""" 
   code scanning:
            1. individuals
               -tip1
               -tip2
               -tip3
            2. public interaction with others on github
               -look for secrets
               ...
            3. publish on pypi
            """)    


with tab3:
   st.write("organisation/podcast/nesletters/how to tackle information fatigue")

# on security when publishing to pypi:
with tab4:
   st.write("maby integrated into tab4?")
   st.write("""
            Open source -> news on security front          
            - pip security
                     - verifikation
                     - trusted authors
            pypi: security update (check release): voluntary two factor authentication requirements. 2fa mandate for critical projects
                     (top 1%)
                     they hand out hardware keys
                     4000 google titan security keys
        """)