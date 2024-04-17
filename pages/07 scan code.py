import streamlit as st

tab0, tab1  = st.tabs(["Reasoning and terminology", "toolbox"])
with tab0: 
      st.markdown("""
### What are some reasons we could want to scan code for?
- Code Quality
- Vulnerability Detection
- Dependency Management
- Compliance and Licensing

It is always important to know what your goal is during scanning. There are three we want to differentiate: 
1. For better quality 
2. To publish it safely to others 
3. To publish it to many others on distribution networks like PyPi 
               
Code Scanners should be a stage in every CI/CD Pipeline and be done regularly and should always be taken seriously. 
                  
It raises the general coding hygiene, which is all the more important in a lax language like python. They can help us uphold certain coding guidelines which can help make our code easier to understand. Even if the only person reading it is ourselves in 6 months! 
                  
Code Scanners also search vor known vulnerabilities in you dependencies, so you do not have to do it all by yourself. Even if you are not sharing your code, chances are high you want to stay safe too.
For this they search through different Community advisory databases and warn when a version of a used package is compromised.
Remember, an advisory is a notification about a vulnerability. You should always think about whether you really want to ignore one.
      
### Vulnerability auditing software
You run this locally as part of your release, your process, your integration tests.
This allows you to be confident that you're not gonna deploy something with a vulnerability.
To audit local environments install it with pip and then run pip-audit.         
Go ahead and run it on your laptop right now and see if up anything installed with a vulnerability.

            """)

with tab1:
      st.markdown("""
As always in live there is a large selection of different code scanners for python.

""")
      

