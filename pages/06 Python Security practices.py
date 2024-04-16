import streamlit as st


tab0, tab1, tab2, tab3, tab4, tab5  = st.tabs(["coding practices","package management", "lockfiles", "hashes", "dependency trees", "tools"])

with tab0:
    st.write("### checklist style (überarbeiten)")
    st.write("""
             draw analogie to basics (update, code analysis, keep secrets, stay informed), \n
             additions when publishing, \n
             additions web apps -> not go into - input validation \n

             1. update your software (manage dependencies)
             2. use antivirus software (scan your code)
             3. new* stay informed (design smart notification system)
        """)
    

    
    

with tab1:
   st.write("### structure of chapter:")
   st.write("""
        proper package management:
         important to look for:
         - lockfiles
         - hashes stored (go through in moment)
         - store dependency trees
    """) # word on python updates -> important too.
   
with tab2:
   st.write("""         
         for environment mangement lockfiles: 
         A lockfile can contain dependency version information that is valid across multiple platforms and Python interpreter versions. 
         Lockfiles are important because they allow for repeatable and deterministic installations. This is most beneficial for applications 
         living at the end of the dependency chain. It can also be useful for internal development and testing of libraries so that 
            other issues can be isolated and reproduced.
         -> many recommendations for uploading to pypi and packaging -> not go into this
         - go through Workflow tools assumption many of you use python for personal projects maby not yet into packaging and publishing tools but still upload code to github 
         and collaborate across public repos
         -> pipenv
         -> poetry
         -> pip-tools
         there are others: like hatch, pdm, rye.. not time to go into all. 
            What we can do: Use lockfiles because version pins, 
         this can f.e. mitigate squat attacks, avoids dependency confusion. 
         

            """)

with tab3:
   st.write(""" hashes
            Hashes verify the file downloaded from PyPI is the same as the version uploaded to PyPI hash computed when uploaded 
            verifies no manipulation/change 

            """)  

with tab4:
   st.write(""" dep trees""")  

with tab5:
   st.write(""" 
            where you are probably at: -> comparison of tools needed?

            - alternative pip-tools -> like to work with pip??
                     -> pip install -> installs into base _> need environments
            -> ok create environment with venv (for Python 3) 
                     python3 -m venv .venv
                     -> activate it now use pip as before
            -> problem? many packages _> make a list in requirements.txt (+ versions)
                     -> use. python3 -m pip install -r requirements.txt
                     and python3 -m pip freeze to get all packages you have installed -> others acn use it too
                     -> updateing becomes very cumbersome -> example in a blog. This loop of dependency conflicts may potentially continue for a long time, and get incredibly tiresome very quickly…
            (https://medium.com/packagr/using-pip-compile-to-manage-dependencies-in-your-python-packages-8451b21a949e)
                     
                     -> alternative: python -m pip install pip-tools
                     but then not have alist of requirements - dynamically want to tupdate your packages?
            
            same procedure for poetry:    
            """)    

# on security when publishing to pypi:
st.write("""
            
    
            1.          
            - pip security
                     - verifikation
                     - trusted authors
            pypi: security update (check release): voluntary two factor authentication requirements. 2fa mandate for critical projects
                     (top 1%)
                     they hand out hardware keys
                     4000 google titan security keys
        """)