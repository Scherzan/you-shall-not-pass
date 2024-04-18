import streamlit as st
import pandas as pd

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
    
#pip = default -manual management
#python -> managed by Pyenv
#Conda package manager in Anaconda can easily manage Python environments and dependencies
#many third party packages that can be used as dependencies. 
#there is not one obvious way to specify dependencies

# how to manage python dependencies -> python version and packages?
# code should always work (can be run without errors) -> coding environment
# what python version
# which packages (also the hidden ones)

with tab1: # integrate"lockfiles", "hashes", "dependency trees"
   st.subheader("Intro Supply Chain Security")
   col1, col2 = st.columns(2)
   with col1:
      criteria = ['manages','can require compilers','package types', "create environment", "dependency checks", "package sources"]
      conda_traits = ["binaries", "no", "any", "yes, built-in", "yes", "Anaconda"]
      pip_traits = ["wheel or source", "yes", "python-only", "no", "no", "PyPi"]
      df_compare= pd.DataFrame.from_records({" ": criteria, "conda": conda_traits, "poetry(+pip)": pip_traits})
      st.table(df_compare)
      st.image("./pages/scripts/assets/env.png")
      # missing text

# add to table: lockfile automation (poetry) Pip and Conda, by default, lack a lock feature
# -> generating lockfiles via installed libraries like pip-tools and conda-lock possible
# dependency conflicts (pip just installs with error messages, conda issues warning and describes which package is installed instead of other version)
# poetry refuses to install -> need to find another option for one or the other.-> more control
# uninstallation of packages: pip only uninstall package nothing else. Conda removes some packages not all dependencies. 
# Poetry remove the package and all its dependencies list of dependencies clutter free.

#Yes, Poetry is compatible with existing projects managed by Pip or Conda. 
#Just initialize your code using Poetry's Poetry.toml format and run it 
#to grab the library of packages and its dependencies, allowing for a seamless transition.


   with col2:
      # missing descriptions
      lockfile = st.checkbox('lockfiles')
      hashes = st.checkbox('hashes')
      dep_tree = st.checkbox('dependency tree')
 # word on python updates -> important too.

   

with tab2:
   st.write(""" 
   code scanning:
            1. individualsto keep your list of 
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