# Code for Streamlit Presentation at PyConDE & PyData Berlin 2024 

![alt text](./pages/assets/mainpage.png " ")

## To Run the Presentation
To see the presentation clone the repo and run:

     poetry shell

to set up the environment.

> ⚠️ This repository depends on old package versions of ```gradio``` and ```pyyaml``` that contain known vulnerabilities. **Be aware that the environment set up installs packages that contain known vulnerabilities** 

Then start the presentation with:

    streamlit run Home.py


## Further Reading
You can find the full list of links to supplementary material and resources in the last tab of the page ```04 Python Security Practices.py```.

A short summary of the list:

### Sofware & Tools

**Before installing a Package from PyPI**  
```guarddog``` (scan PyPi package before installing them):
https://github.com/DataDog/guarddog  
```phylium``` (sandbox environment to test package installations):  https://blog.phylum.io/sandboxing-package-installations-arms-developers-with-defense-against-open-source-attacks-and-unintended-consequences/  

**After installing from PyPI**  
```bandit``` (code scanner for vulnerabilities): https://bandit.readthedocs.io/en/latest/  
```pip-audit``` (dependency scanner): https://pypi.org/project/pip-audit/  
```pip-tools``` (general dependency management): https://pip-tools.readthedocs.io/en/stable/  
```jake``` (dependency scanner with conda support): https://github.com/sonatype-nexus-community/jake  
```snyk VSCode extension``` (fully integrated code scan for repositories): https://snyk.io/  

**Other**  
```Semgrep``` (code scanning and code rule database): https://github.com/semgrep/semgrep  
*Semgrep Playground* (database on potentially harmfull code patterns): https://semgrep.dev/playground/new  
```badsecrets``` (scans for leaked and knwon secrets): https://github.com/blacklanternsecurity/badsecrets  

### Databases
CVE (official vulnerability database: https://www.cve.org/  

### Information & Organisations
Python Software Foundation (reporting vulnerabilities): https://www.python.org/dev/security/    
OWASP-Cheat Sheet Series (collection of specific application security topics): https://cheatsheetseries.owasp.org/  
Python Software Foundation Open Source Security Efforts: https://pyfound.blogspot.com/2024/04/new-open-initiative-for-cybersecurity.html P  

### Blogs
**The Python Package Index Blog** (curated news on PyPi specific issues): https://blog.pypi.org/  
**GitGuardian Blog**: https://blog.gitguardian.com/
**Phylium Research Blog** (security reasearch): https://blog.phylum.io/tag/research/  
**Snyk Blog** (articels among others on AI topcs): https://snyk.io/blog/  

### Talks
Software Supply Chain Security: https://www.youtube.com/watch?v=i1QqhGsbX6Y and https://www.youtube.com/watch?v=VWWgkF-0cDQ   

### Education IT-Security
EDX Course on IT-Security (Tel Aviv University): https://www.edx.org/certificates/professional-certificate/taux-unlocking-information-security






