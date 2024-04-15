import streamlit as st

tab0, tab1, tab2, tab3, tab4, tab5  = st.tabs(["risk mitigation","package management", "lockfiles", "hashes", "dependency trees", "package management"])

with tab0:
    st.write("### structure of chapter:")
    st.write("""
            1. proper package management:
             2. scan for vulnerabilities of code (before commiting/publshing anywhere)
             3. stay informed (tackle info fatigue) + ressources
        """)
    
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
    
    

with tab1:
   st.write("### structure of chapter:")
   st.write("""
        proper package management:
         important to look for:
         - lockfiles
         - hashes stored (go through in moment)
         - store dependency trees
    """)
   
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
         -> conda: 
            - conda can create an environment file in the yaml format to distribute to others using also conda. Create it using: 
               - conda env export > environment.yml
            - and then create a new environment with
               - conda env create -f environment.yaml
            - now you can share the yaml-file with everyone. If you only want to adapt to updates you need the following command:
               - conda env update --file environment.yml --prune
            - you can actually use pip inside of conda and have access to many of pips features (although it can make it own problems)
            - Condas biggest selling point is its large usage in scientific computing and AI. The big community with this focus uses conda and develops it with this use case in mind.
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
   st.title(""" Dependency Trees""") 
   st.markdown(""" Python is a highly interdependent language and we all use many packages without giving it much thought. 
This builds a big pile of libraries that accumulate in even smaller scripts to the point that it gave birth to a whole landscape of package management systems like pip, poetry, conda and much more.
Most of the times the dependencies will be displayed in a requirements file or as a list of actively installed packages.
But this only gives an impression of either the surface or the final picture.
You won't know why a package X is ACTUALLY needed in your code if you did not actively imported it.
Dependency Trees are a way to display all the packages your code needs, along with their path into the environment.

Lets say you have two known dependencies for package A und B, a DT might look like this
- A
   - C
   - D
      - E
- B
   - C

This gives a much clearer overview which package is actively installed and required and which is only a dependent.

And while these structures are essential for the package management systems itself, most Developers do not keep track of them.
But with them we can now see in detail which package forces us to use a certain Version of another package.
This becomes very important if we come across vulnerabilities and want to update to a newer version.
Because now we know which higher-leveled package we might actually need to update in order to increase the version of a dependent package.
               
Since this is such a relevant functionality for package management systems, they can (as far as we are aware) all produce them with ease. 
               
Here is the command in poetry:
""")
# Verbally: with these structures conflict resolution is achieved by finding all requirements for a certain package an then trying to fulfill them all
   st.code("""
   poetry show --tree
   """, 
         language='bash')
   st.write("And in conda it looks similar:")
   st.code("""
   conda list --tree
   """, 
         language='bash')
   st.write("pip and also pip-tools need another package called pipdeptree:")
   st.code("""
   pip install pipdeptree
   pipdeptree
   """, 
         language='bash')
   st.write("pipenv makes it the easiest:")
   st.code("""
   pipenv graph
   """, 
         language='bash')
   st.write("The resulting tree will always look the same and can be searched, even if most sophisticated security tools should do this for you, it never hurts to know where to look yourself if something needs to be done")

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
