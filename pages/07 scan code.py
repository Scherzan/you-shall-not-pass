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
- Remind you of your favorite task: Code documentation
- They help us uphold certain coding guidelines which can help make our code easier to understand. Even if the only person reading it is ourselves in 6 months! 
- Reduce Code smells
- Makes it easier to have a basic overview over dependencies and known vulnerabilities

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

If you publish your code, most likely via Github or Lab, you should automate your chosen scanners. 
- don't have to do many scanners one by one but instead have an automated pipeline
- can prohibit merges unless certain quality and safety criteria are met. 
- have an indicator for others that your code is actually well done
- one time investment, that can be the baseline for your knowledge about CI/CD

#### Publish your Code on PyPi

PyPi has a really low requirement to publish, which is great to have as many contributors as possible. But this makes it easier for bad actors, active ones or not.

We are all good, moral people

=> We would only publish packages that are as safe, clean and reliable as possible

=> We need to hold ourselves to a very high standard and enforce it for ourselves before publishing packages for others

 """)
      

