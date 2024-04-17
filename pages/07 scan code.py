import streamlit as st

st.markdown(
"""
### Why and for what should we scan our code?
- Enhance Code Quality
- automatic Vulnerability Detection
- Dependency Management
- Compliance and Licensing

It is always important to know what your goal is during scanning. There are three we want to differentiate: 
- For ourself
- To publish it safely to others (like via github) 
- To publish it to many others on distribution networks like PyPi 

#### Scan your own Code for your own sake

If we Code for ourself we still want to create the best code we can. 

Advantages for Code scanners even for your self:
- They raise the general coding hygiene, which is all the more important in a lax language like python. 
- They help us uphold certain coding guidelines which can help make our code easier to understand. Even if the only person reading it is ourselves in 6 months! 
- Reduce Code smells

Scanners that specialize in this use case are also known as linters. Most IDEs have linters integrated but you should make sure to adapt them to your own style.
There are many linters to choose from and there are as always debates about which is the best. But nothing is stopping you from using two or more at the same time. Some Linters that are widely used are: 
- Pylint => do example
- Flake8
- pycodestyle
- pylama (actually combines many linters and other tools)

A different specialization got more into the complexity of your code. They warn you once your modules and classes reach a certain complexity threshold. This can be defined by different measures, like lines of code in a file/class/function or the depth of your loops and if-clauses. Examples are:
- Radon 
- Xenon => do example

            
Other Code Scanners also search for known vulnerabilities in your dependencies and other security risks. Even in a project thats only for yourself, if there is some kind of network connection involved, you want to be as secure as possible. Known security scanners are: 
- Safety => do example
- Bandit

#### Publishing Code

Publish code => automate
baseline CI/CD
pipeline your scanners
set thresholds prohibit commits/merges

#### Publish your Code on PyPi

PyPi has a REALLY low requirement to publish
you are all nice people, so you WANT safe code => YOU have to hold your packages to a very high standard
(although this is beginning to change)

 """)
      

