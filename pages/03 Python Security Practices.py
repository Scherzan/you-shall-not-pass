import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide",
)


tab0, tab1, tab2, tab3, tab4  = st.tabs(["Where do I start?", "I have my code in a GitHub repo...", "How to check pip packages before installing?", "What to look for in dependency management?", "Where can I find more information?"])


# Prepared a pseudo FAQ
with tab0:
   if "bandit_on" not in st.session_state:
      st.session_state["bandit_on"] = False
   if "safety_on" not in st.session_state:
      st.session_state["safety_on"] = False
   if "github_action" not in st.session_state:
      st.session_state["github_action"] = False


   def switch_click(input):
      switches = ["bandit_on", "radon_on", "safety_on", "github_action"]
      switches.remove(input)
      for switch in switches:
         st.session_state[switch] = False
      st.session_state[input] = not st.session_state[input]


   st.markdown(
   """
   ### How about Code scanning
   - They raise the general coding hygiene
   - Reduce Code smells
   - Many automatically show possible vulnerabilites
   - Makes it easier to have a basic overview over dependencies and known vulnerabilities with static code scanners

   #### There are many linters to choose from:
   - Pylint 
   - Flake8
   - pycodestyle
   - pylama (actually combines many linters and other tools)
   - Bandit
   """) 
      
   st.button("Show Bandit example", on_click=switch_click, args=["bandit_on"])

   with open("code_scanners_examples/bandit_report.txt", "r") as file:
      bandit_contents = file.read()
   if st.session_state["bandit_on"]:
      st.code(bandit_contents, language="bash")
      st.button("Hide Bandit example", on_click=switch_click, args=["bandit_on"])   
   
   st.markdown("""
   #### Dependency scanners, that search your tree known CVEs and other risks:
   - Safety 
   - Dependency-Check
   - pip-audit
   
   Find a comprehensive list here: https://owasp.org/www-community/Source_Code_Analysis_Tools
   """)

with tab1:
   st.markdown("""
   ### Using Git repositories:
   - automate chosen scanners and use an automated pipeline
   - configure merges requirements to meet security standards 
   - have an indicator for others that your code is actually well done (add example)
   - check ressources on CI/CD
   - dig deep into dependency management -> reference Anto
   - Compliance and Licensing -> mention tools for license checking?
   """)

   st.markdown("#### Github action example to follow:")
   st.button("show Github actions example", on_click=switch_click, args=["github_action"])

   with open(".github/workflows/main.yml", "r") as file:
      action_content = file.read()
   if st.session_state["github_action"]:
      st.code(action_content, language="yaml")
      st.button("Hide Github actions example", on_click=switch_click, args=["github_action"])

   st.markdown("""
   ### I want to publish my Code as a package on PyPi?
   - automate chosen scanners 
   - use automated pipeline
   - PyPi Account since beginning of the year with 2FA  
   - Check workflow here: https://packaging.python.org/en/latest/tutorials/packaging-projects/
   - generally there are low requirement to publish on PyPi (It makes it easy for us and for bad actors)
   """)

with tab2:
   st.markdown("### I googeled how to ... and the solution suggests to pip install some package.")
   col1, col2 = st.columns(2)
   with col1:
      caution = st.checkbox("Be cautious, visit the page and check for a git repository.")
      if caution:
          auditing = st.checkbox("Check for high risk python expressions such as subprocess.run, exec and eval functions.")
          if auditing:
              init_check = st.checkbox("Check common places for malicious code in __init__.py file or setup.py.")
              if init_check:
                  check_for_http = st.checkbox("Check for http requests exfiltrating system information.")
                  with col2:
                     if check_for_http:
                        st.image("./pages/assets/git_search.png")

   st.markdown("### I am still not confident or want more proof.")
   col1, col2 = st.columns(2)
   with col1:   
      check_vulnerability_db = st.checkbox("Check databse for reports on the package: i.e. snyk database.")
      if check_vulnerability_db:
          st.write("https://security.snyk.io/vuln/pip")
          with col2:
            st.image("./pages/assets/search_snyk.png")
          automated_pypi_check = st.checkbox("Identify malicious PyPI packages before download with guardDog.")
          if automated_pypi_check:
             st.write("guardDog: https://github.com/DataDog/guarddog")
             download_check = st.checkbox("Download latest package version from pypi and run code checks on code base.")
             if download_check:
                st.write("Local code scan i.e. with Safety.")

   st.markdown("### I want to try out risky packages.")
   use_phylium = st.checkbox("Use a sandbox environment i.e. phylum CLI with poetry support.")
   if use_phylium:
      st.write("Sanbox package installations: https://blog.phylum.io/sandboxing-package-installations-arms-developers-with-defense-against-open-source-attacks-and-unintended-consequences/")
   

with tab3:
   st.markdown("### Dependency management is key.")
   col1, col2 = st.columns(2)
   with col1:
      dep_management = st.checkbox("Make sure you have repeatable and deterministic installations.") 
      if dep_management:
         lockfiles = st.checkbox("Use Lockfiles with pinned package versions, hashes and the full dependency tree.)", value=True)
         requirements_file = st.checkbox("requirements.txt", value=True)

         with col2:
            if requirements_file:
               st.code("""
                      # strict dependencies
                      aiofiles==23.2.1\n
                      altair==5.3.0\n
                      annotated-types==0.6.0\n
                      ...
                      # loose dependencies
                      Authlib
                      blinker
                      cachetools""")
      
   scan_dep = st.checkbox("Use a tool like pip-audit to scan your dependencies before going public.")
   if scan_dep:
      st.image("./pages/assets/pip_audit.png")

   advanced = st.checkbox("Advanced: Using your own pypi repo locally (more a company level solution).")


with tab4:
   col1, col2 = st.columns(2)
   with col1:
      st.header("Tools & Ressources:")
      st.subheader("Software")
      st.write("GuardDog: https://github.com/DataDog/guarddog")
      st.write("Sanbox package installations: https://blog.phylum.io/sandboxing-package-installations-arms-developers-with-defense-against-open-source-attacks-and-unintended-consequences/")
      st.write("Semgrep Playground for code security heuristics: https://semgrep.dev/playground/new")
      st.write("Pip dependency management tools: https://pip-tools.readthedocs.io/en/stable/")
      #st.write("Scan for leaked secrets: https://github.com/blacklanternsecurity/badsecrets (we did not test this)")
      st.subheader("Databases")
      st.write("https://www.cve.org/ Official vulnerability Database (Search for Python)")
      st.write("https://security.snyk.io/ Based on CVE database with extended information on Poc and Fixes")
      st.subheader("Get involved:")
      st.write("Get startet with ethical hacking: https://snyk.io/ethical-hacking-resources/")
      st.write("Python Software Foundation. https://www.python.org/psf/get-involved/")
      st.subheader("Organisations & Ressources")
      st.write("https://cheatsheetseries.owasp.org/ Collection of specific application security topics")
      st.write("https://www.python.org/dev/security/ Reporting Security Issues with PyPi")
      st.write("https://pyfound.blogspot.com/2024/04/new-open-initiative-for-cybersecurity.html Python Software Foundation Open Source Security Efforts")   
      

   with col2:
      st.markdown("#")
      st.markdown("#")
      st.subheader("Blogs")
      st.write("The Python Package Index Blog: https://blog.pypi.org/ (Well curated news on PyPi specific issues)")
      st.write("GitGuardian Blog: https://blog.gitguardian.com/")
      st.write("Phylium Research Blog: https://blog.phylum.io/tag/research/ (Security Reasearch)")
      st.write("Snyk Blog: https://snyk.io/blog/ (Variety of  Articels also on AI topcs i.e. Using Copilot)")
      st.subheader("Podcasts")
      st.write("The Real Python Podcast: https://realpython.com/podcasts/rpp/114/ (Remember to check shownotes.)")
      st.write("Long list: https://blog.phylum.io/the-power-of-the-pod/")
      st.subheader("Talks")
      st.write(""" 
               https://www.youtube.com/watch?v=i1QqhGsbX6Y \n
               https://www.youtube.com/watch?v=VWWgkF-0cDQ
               """)


