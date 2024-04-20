import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide",
)


tab0, tab1, tab2, tab3, tab4  = st.tabs(["coding practices", "code scan", "package management", "pypi and open source", "stay informed"])


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



   

with tab1:
   if "pylint_on" not in st.session_state:
      st.session_state["pylint_on"] = False
   if "safety_on" not in st.session_state:
      st.session_state["safety_on"] = False
   if "github_action" not in st.session_state:
      st.session_state["github_action"] = False


   def switch_click(input):
      switches = ["pylint_on", "radon_on", "safety_on", "github_action"]
      switches.remove(input)
      for switch in switches:
         st.session_state[switch] = False
      st.session_state[input] = not st.session_state[input]


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
   - Reduce Code smells
   - Makes it easier to have a basic overview over dependencies and known vulnerabilities

   Scanners that specialize in increasing your general code quality are also known as linters.
   There are many linters to choose from:
   - Pylint 
   - Flake8
   - pycodestyle
   - pylama (actually combines many linters and other tools)
   """)
      

   st.button("Activate Pylint example", on_click=switch_click, args=["pylint_on"])

   if st.session_state["pylint_on"]:
      st.code("""
   pylint code_scanners_examples/bad_linting.py 
               
   ************* Module bad_linting
   code_scanners_examples/bad_linting.py:16:0: W0311: Bad indentation. Found 2 spaces, expected 4 (bad-indentation)
   code_scanners_examples/bad_linting.py:28:0: C0301: Line too long (168/100) (line-too-long)
   code_scanners_examples/bad_linting.py:32:0: W0311: Bad indentation. Found 2 spaces, expected 4 (bad-indentation)
   code_scanners_examples/bad_linting.py:34:0: C0304: Final newline missing (missing-final-newline)
   code_scanners_examples/bad_linting.py:34:0: W0311: Bad indentation. Found 2 spaces, expected 4 (bad-indentation)
   code_scanners_examples/bad_linting.py:1:0: C0114: Missing module docstring (missing-module-docstring)
   code_scanners_examples/bad_linting.py:1:0: C0116: Missing function or method docstring (missing-function-docstring)
   code_scanners_examples/bad_linting.py:4:0: C0103: Constant name "result" doesn't conform to UPPER_CASE naming style (invalid-name)
   code_scanners_examples/bad_linting.py:8:0: C0103: Constant name "unused_variable" doesn't conform to UPPER_CASE naming style (invalid-name)
   code_scanners_examples/bad_linting.py:11:0: C0116: Missing function or method docstring (missing-function-docstring)
   code_scanners_examples/bad_linting.py:11:0: C0103: Function name "InvalidFunctionName" doesn't conform to snake_case naming style (invalid-name)
   code_scanners_examples/bad_linting.py:15:0: C0116: Missing function or method docstring (missing-function-docstring)
   code_scanners_examples/bad_linting.py:19:6: E0602: Undefined variable 'undefined_variable' (undefined-variable)
   code_scanners_examples/bad_linting.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
   code_scanners_examples/bad_linting.py:28:0: C0103: Constant name "long_variable_name_for_testing_purpose" doesn't conform to UPPER_CASE naming style (invalid-name)

   -----------------------------------
   Your code has been rated at 0.00/10""", language="bash")

   st.markdown("""
   Other Code Scanners search for known vulnerabilities in your dependencies and other security risks. Examples are are: 
   - Safety => do example
   - Bandit
   """)

   st.button("Activate Safety example", on_click=switch_click, args=["safety_on"])
   if st.session_state["safety_on"]:
      st.markdown("""
   safety check -r code_scanners_examples/bad_requirements.txt
   +==============================================================================================================================================================================================================+
                  
                                 /$$$$$$            /$$
                                 /$$__  $$          | $$
            /$$$$$$$  /$$$$$$ | $$  \__//$$$$$$  /$$$$$$   /$$   /$$
            /$$_____/ |____  $$| $$$$   /$$__  $$|_  $$_/  | $$  | $$
            |  $$$$$$   /$$$$$$$| $$_/  | $$$$$$$$  | $$    | $$  | $$
            \____  $$ /$$__  $$| $$    | $$_____/  | $$ /$$| $$  | $$
            /$$$$$$$/|  $$$$$$$| $$    |  $$$$$$$  |  $$$$/|  $$$$$$$
            |_______/  \_______/|__/     \_______/   \___/   \____  $$
                                                            /$$  | $$
                                                            |  $$$$$$/
   by safetycli.com                                        \______/

   +==============================================================================================================================================================================================================+

   REPORT 

   Safety is using PyUp's free open-source vulnerability database. This data is 30 days old and limited. 
   For real-time enhanced vulnerability data, fix recommendations, severity reporting, cybersecurity support, team and project policy management and more sign up at https://pyup.io or email
   sales@pyup.io

   Safety v3.1.0 is scanning for Vulnerabilities...
   Scanning dependencies in your files:

   -> code_scanners_examples/bad_requirements.txt

   Using open-source vulnerability database
   Found and scanned 2 packages
   Timestamp 2024-04-17 22:38:53
   30 vulnerabilities reported
   0 vulnerabilities ignored

   +==============================================================================================================================================================================================================+
   VULNERABILITIES REPORTED 
   +==============================================================================================================================================================================================================+

   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 39646
      Affected spec: <2.2.19
      ADVISORY: Django versions 2.2.19, 3.0.13 and 3.1.7 include a fix for CVE-2021-23336: Web cache poisoning via 'django.utils.http.limited_parse_qsl()'. Django contains a copy of
      'urllib.parse.parse_qsl' which was added to backport some security fixes. A further security fix has been issued recently such that 'parse_qsl(' no longer allows using ';' as a query parameter...
      CVE-2021-23336
      For more information about this vulnerability, visit https://data.safetycli.com/v/39646/97c
      To ignore this vulnerability, use PyUp vulnerability id 39646 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 40637
      Affected spec: <2.2.24
      ADVISORY: Django before 2.2.24, 3.x before 3.1.12, and 3.2.x before 3.2.4 has a potential directory traversal via django.contrib.admindocs. Staff members could use the TemplateDetailView view to
      check the existence of arbitrary files. Additionally, if (and only if) the default admindocs templates have been customized by application developers to also show file contents, then not only the...
      CVE-2021-33203
      For more information about this vulnerability, visit https://data.safetycli.com/v/40637/97c
      To ignore this vulnerability, use PyUp vulnerability id 40637 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 40638
      Affected spec: <2.2.24
      ADVISORY: Django 2.2.24, 3.1.12, and 3.2.4 include a fix for CVE-2021-33571: In Django 2.2 before 2.2.24, 3.x before 3.1.12, and 3.2 before 3.2.4, URLValidator, validate_ipv4_address, and
      validate_ipv46_address do not prohibit leading zero characters in octal literals. This may allow a bypass of access control that is based on IP addresses. (validate_ipv4_address and...
      CVE-2021-33571
      For more information about this vulnerability, visit https://data.safetycli.com/v/40638/97c
      To ignore this vulnerability, use PyUp vulnerability id 40638 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 55264
      Affected spec: <3.2.19
      ADVISORY: Django 4.2.1, 4.1.9 and 3.2.19 include a fix for CVE-2023-31047: In Django 3.2 before 3.2.19, 4.x before 4.1.9, and 4.2 before 4.2.1, it was possible to bypass validation when using
      one form field to upload multiple files. This multiple upload has never been supported by forms.FileField or forms.ImageField (only the last uploaded file was validated). However, Django's "Uploading...
      CVE-2023-31047
      For more information about this vulnerability, visit https://data.safetycli.com/v/55264/97c
      To ignore this vulnerability, use PyUp vulnerability id 55264 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 61586
      Affected spec: <3.2.22
      ADVISORY: Django 4.2.6, 4.1.12 and 3.2.22 include a fix for CVE-2023-43665: Denial-of-service possibility in django.utils.text.Truncator. The django.utils.text.Truncator chars() and words()
      methods (when used with html=True) are subject to a potential DoS (denial of service) attack via certain inputs with very long, potentially malformed HTML text. The chars() and words() methods are...
      CVE-2023-43665
      For more information about this vulnerability, visit https://data.safetycli.com/v/61586/97c
      To ignore this vulnerability, use PyUp vulnerability id 61586 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 38749
      Affected spec: <2.2.16
      ADVISORY: Django 2.2.16, 3.0.10 and 3.1.1 include a fix for CVE-2020-24583: An issue was discovered in Django 2.2 before 2.2.16, 3.0 before 3.0.10, and 3.1 before 3.1.1 (when Python 3.7+ is
      used). FILE_UPLOAD_DIRECTORY_PERMISSIONS mode was not applied to intermediate-level directories created in the process of uploading files. It was also not applied to intermediate-level collected...
      CVE-2020-24583
      For more information about this vulnerability, visit https://data.safetycli.com/v/38749/97c
      To ignore this vulnerability, use PyUp vulnerability id 38749 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 38752
      Affected spec: <2.2.16
      ADVISORY: An issue was discovered in Django 2.2 before 2.2.16, 3.0 before 3.0.10, and 3.1 before 3.1.1 (when Python 3.7+ is used). The intermediate-level directories of the filesystem cache had
      the system's standard umask rather than 0o077.
      CVE-2020-24584
      For more information about this vulnerability, visit https://data.safetycli.com/v/38752/97c
      To ignore this vulnerability, use PyUp vulnerability id 38752 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 59293
      Affected spec: <3.2.20
      ADVISORY: Django 3.2.20, 4.1.10 and 4.2.3 include a fix for CVE-2023-36053: EmailValidator and URLValidator are subject to a potential ReDoS (regular expression denial of service) attack via a
      very large number of domain name labels of emails and URLs.https://www.djangoproject.com/weblog/2023/jul/03/security-releases
      CVE-2023-36053
      For more information about this vulnerability, visit https://data.safetycli.com/v/59293/97c
      To ignore this vulnerability, use PyUp vulnerability id 59293 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 39594
      Affected spec: <2.1.9
      ADVISORY: Django versions 2.1.9 and 2.2.2 include a patched bundled jQuery version to avoid a Prototype Pollution vulnerability.
      CVE-2019-11358
      For more information about this vulnerability, visit https://data.safetycli.com/v/39594/97c
      To ignore this vulnerability, use PyUp vulnerability id 39594 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 44427
      Affected spec: <2.2.26
      ADVISORY: Django 2.2.26, 3.2.11 and 4.0.1 include a fix for CVE-2021-45116: An issue was discovered in Django 2.2 before 2.2.26, 3.2 before 3.2.11, and 4.0 before 4.0.1. Due to leveraging the
      Django Template Language's variable resolution logic, the dictsort template filter was potentially vulnerable to information disclosure, or an unintended method call, if passed a suitably crafted...
      CVE-2021-45116
      For more information about this vulnerability, visit https://data.safetycli.com/v/44427/97c
      To ignore this vulnerability, use PyUp vulnerability id 44427 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 44423
      Affected spec: <2.2.26
      ADVISORY: Django 2.2.26, 3.2.11 and 4.0.1 include a fix for CVE-2021-45115: UserAttributeSimilarityValidator incurred significant overhead in evaluating a submitted password that was
      artificially large in relation to the comparison values. In a situation where access to user registration was unrestricted, this provided a potential vector for a denial-of-service...
      CVE-2021-45115
      For more information about this vulnerability, visit https://data.safetycli.com/v/44423/97c
      To ignore this vulnerability, use PyUp vulnerability id 44423 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 44426
      Affected spec: <2.2.26
      ADVISORY: Django 2.2.26, 3.2.11 and 4.0.1 include a fix for CVE-2021-45452: Storage.save in Django 2.2 before 2.2.26, 3.2 before 3.2.11, and 4.0 before 4.0.1 allows directory traversal if
      crafted filenames are directly passed to it.https://www.djangoproject.com/weblog/2022/jan/04/security-releases/
      CVE-2021-45452
      For more information about this vulnerability, visit https://data.safetycli.com/v/44426/97c
      To ignore this vulnerability, use PyUp vulnerability id 44426 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 62126
      Affected spec: <3.2.23
      ADVISORY: Django 4.2.7, 4.1.13 and 3.2.23 include a fix for CVE-2023-46695: Potential denial of service vulnerability in UsernameField on
      Windows.https://www.djangoproject.com/weblog/2023/nov/01/security-releases
      CVE-2023-46695
      For more information about this vulnerability, visit https://data.safetycli.com/v/62126/97c
      To ignore this vulnerability, use PyUp vulnerability id 62126 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 52945
      Affected spec: <3.2.17
      ADVISORY: Django 3.2.17, 4.0.9 and 4.1.6 includes a fix for CVE-2023-23969: In Django 3.2 before 3.2.17, 4.0 before 4.0.9, and 4.1 before 4.1.6, the parsed values of Accept-Language headers are
      cached in order to avoid repetitive parsing. This leads to a potential denial-of-service vector via excessive memory usage if the raw value of Accept-Language headers is very...
      CVE-2023-23969
      For more information about this vulnerability, visit https://data.safetycli.com/v/52945/97c
      To ignore this vulnerability, use PyUp vulnerability id 52945 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 64976
      Affected spec: <3.2.24
      ADVISORY: Affected versions of Django are vulnerable to potential denial-of-service in intcomma template filter when used with very long strings.
      CVE-2024-24680
      For more information about this vulnerability, visit https://data.safetycli.com/v/64976/97c
      To ignore this vulnerability, use PyUp vulnerability id 64976 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 48041
      Affected spec: <2.2.28
      ADVISORY: Django 2.2.28, 3.2.13 and 4.0.4 include a fix for CVE-2022-28346: An issue was discovered in Django 2.2 before 2.2.28, 3.2 before 3.2.13, and 4.0 before 4.0.4. QuerySet.annotate(),
      aggregate(), and extra() methods are subject to SQL injection in column aliases via a crafted dictionary (with dictionary expansion) as the passed...
      CVE-2022-28346
      For more information about this vulnerability, visit https://data.safetycli.com/v/48041/97c
      To ignore this vulnerability, use PyUp vulnerability id 48041 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 48040
      Affected spec: <2.2.28
      ADVISORY: Django 2.2.28, 3.2.13 and 4.0.4 include a fix for CVE-2022-28347: A SQL injection issue was discovered in QuerySet.explain() in Django 2.2 before 2.2.28, 3.2 before 3.2.13, and 4.0
      before 4.0.4. This occurs by passing a crafted dictionary (with dictionary expansion) as the **options argument, and placing the injection payload in an option...
      CVE-2022-28347
      For more information about this vulnerability, visit https://data.safetycli.com/v/48040/97c
      To ignore this vulnerability, use PyUp vulnerability id 48040 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 65771
      Affected spec: <3.2.25
      ADVISORY: Affected versions of Django are vulnerable to potential regular expression denial-of-service. django.utils.text.Truncator.words() method (with html=True) and truncatewords_html
      template filter were subject to a potential regular expression denial-of-service attack using a suitably crafted string (follow up to CVE-2019-14232 and CVE-2023-43665).
      CVE-2024-27351
      For more information about this vulnerability, visit https://data.safetycli.com/v/65771/97c
      To ignore this vulnerability, use PyUp vulnerability id 65771 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 44742
      Affected spec: <2.2.27
      ADVISORY: The {% debug %} template tag in Django 2.2 before 2.2.27, 3.2 before 3.2.12, and 4.0 before 4.0.2 does not properly encode the current context. This may lead to XSS.
      CVE-2022-22818
      For more information about this vulnerability, visit https://data.safetycli.com/v/44742/97c
      To ignore this vulnerability, use PyUp vulnerability id 44742 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 44741
      Affected spec: <2.2.27
      ADVISORY: Django 2.2.27, 3.2.12 and 4.0.2 include a fix for CVE-2022-23833: Denial-of-service possibility in file uploads.https://www.djangoproject.com/weblog/2022/feb/01/security-releases
      CVE-2022-23833
      For more information about this vulnerability, visit https://data.safetycli.com/v/44741/97c
      To ignore this vulnerability, use PyUp vulnerability id 44741 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 40404
      Affected spec: <2.2.21
      ADVISORY: Django 2.2.21, 3.1.9 and 3.2.1 include a fix for CVE-2021-31542: MultiPartParser, UploadedFile, and FieldFile allowed directory traversal via uploaded files with suitably crafted file
      names.https://www.djangoproject.com/weblog/2021/may/04/security-releases
      CVE-2021-31542
      For more information about this vulnerability, visit https://data.safetycli.com/v/40404/97c
      To ignore this vulnerability, use PyUp vulnerability id 40404 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 49733
      Affected spec: <3.2.14
      ADVISORY: Django 3.2.14 and 4.0.6 include a fix for CVE-2022-34265: Potential SQL injection via Trunc(kind) and Extract(lookup_name)
      arguments.https://www.djangoproject.com/weblog/2022/jul/04/security-releases
      CVE-2022-34265
      For more information about this vulnerability, visit https://data.safetycli.com/v/49733/97c
      To ignore this vulnerability, use PyUp vulnerability id 49733 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 51340
      Affected spec: <3.2.16
      ADVISORY: In Django 3.2 before 3.2.16, 4.0 before 4.0.8, and 4.1 before 4.1.2, internationalized URLs were subject to a potential denial of service attack via the locale parameter, which is
      treated as a regular expression.
      CVE-2022-41323
      For more information about this vulnerability, visit https://data.safetycli.com/v/51340/97c
      To ignore this vulnerability, use PyUp vulnerability id 51340 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 43041
      Affected spec: <2.2.25
      ADVISORY: Django versions 2.2.25, 3.1.14 and 3.2.10 include a fix for CVE-2021-44420: In Django 2.2 before 2.2.25, 3.1 before 3.1.14, and 3.2 before 3.2.10, HTTP requests for URLs with trailing
      newlines could bypass upstream access control based on URL paths.https://www.djangoproject.com/weblog/2021/dec/07/security-releases/
      CVE-2021-44420
      For more information about this vulnerability, visit https://data.safetycli.com/v/43041/97c
      To ignore this vulnerability, use PyUp vulnerability id 43041 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 60956
      Affected spec: <3.2.21
      ADVISORY: Django 3.2.21, 4.1.11 and 4.2.5 include a fix for CVE-2023-41164: Potential denial of service vulnerability in
      django.utils.encoding.uri_to_iri().https://www.djangoproject.com/weblog/2023/sep/04/security-releases
      CVE-2023-41164
      For more information about this vulnerability, visit https://data.safetycli.com/v/60956/97c
      To ignore this vulnerability, use PyUp vulnerability id 60956 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 50454
      Affected spec: <3.2.15
      ADVISORY: Django 3.2.15 and 4.0.7 include a fix for CVE-2022-36359: An issue was discovered in the HTTP FileResponse class in Django 3.2 before 3.2.15 and 4.0 before 4.0.7. An application is
      vulnerable to a reflected file download (RFD) attack that sets the Content-Disposition header of a FileResponse when the filename is derived from user-supplied...
      CVE-2022-36359
      For more information about this vulnerability, visit https://data.safetycli.com/v/50454/97c
      To ignore this vulnerability, use PyUp vulnerability id 50454 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in django version 1.11.29
      Vulnerability ID: 53315
      Affected spec: <3.2.18
      ADVISORY: Django 4.1.7, 4.0.10 and 3.2.18 include a fix for CVE-2023-24580: Potential denial-of-service vulnerability in file uploads.https://www.djangoproject.com/weblog/2023/feb/14/security-
      releases
      CVE-2023-24580
      For more information about this vulnerability, visit https://data.safetycli.com/v/53315/97c
      To ignore this vulnerability, use PyUp vulnerability id 53315 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in flask version 0.10.1
      Vulnerability ID: 55261
      Affected spec: <2.2.5
      ADVISORY: Flask 2.2.5 and 2.3.2 include a fix for CVE-2023-30861: When all of the following conditions are met, a response containing data intended for one client may be cached and subsequently
      sent by the proxy to other clients. If the proxy also caches 'Set-Cookie' headers, it may send one client's 'session' cookie to other clients. The severity depends on the application's use of the...
      CVE-2023-30861
      For more information about this vulnerability, visit https://data.safetycli.com/v/55261/97c
      To ignore this vulnerability, use PyUp vulnerability id 55261 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in flask version 0.10.1
      Vulnerability ID: 36388
      Affected spec: <0.12.3
      ADVISORY: flask version Before 0.12.3 contains a CWE-20: Improper Input Validation vulnerability in flask that can result in Large amount of memory usage possibly leading to denial of service.
      This attack appear to be exploitable via Attacker provides JSON data in incorrect encoding. This vulnerability appears to have been fixed in 0.12.3.
      CVE-2018-1000656
      For more information about this vulnerability, visit https://data.safetycli.com/v/36388/97c
      To ignore this vulnerability, use PyUp vulnerability id 36388 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   -> Vulnerability found in flask version 0.10.1
      Vulnerability ID: 38654
      Affected spec: <0.12.3
      ADVISORY: Flask 0.12.3 includes a fix for CVE-2019-1010083: Unexpected memory usage. The impact is denial of service. The attack vector is crafted encoded JSON data. NOTE: this may overlap
      CVE-2018-1000656.https://github.com/pallets/flask/pull/2695/commits/0e1e9a04aaf29ab78f721cfc79ac2a691f6e3929
      CVE-2019-1010083
      For more information about this vulnerability, visit https://data.safetycli.com/v/38654/97c
      To ignore this vulnerability, use PyUp vulnerability id 38654 in safety’s ignore command-line argument or add the ignore to your safety policy file.


   +==============================================================================================================================================================================================================+
      REMEDIATIONS

   30 vulnerabilities were reported in 2 packages. For detailed remediation & fix recommendations, upgrade to a commercial license. 

   +==============================================================================================================================================================================================================+

   Scan was completed. 30 vulnerabilities were reported. 

   +==============================================================================================================================================================================================================+

   Safety is using PyUp's free open-source vulnerability database. This data is 30 days old and limited. 
   For real-time enhanced vulnerability data, fix recommendations, severity reporting, cybersecurity support, team and project policy management and more sign up at https://pyup.io or email
   sales@pyup.io

   +==============================================================================================================================================================================================================+""")


   st.markdown("""
   #### Publishing Code

   If you publish your code, most likely via Github or Lab, you should automate your chosen scanners. 
   - don't have to do many scanners one by one but instead have an automated pipeline
   - can prohibit merges unless certain quality and safety criteria are met. 
   - have an indicator for others that your code is actually well done
   - one time investment, that can be the baseline for your knowledge about CI/CD
   """)

   st.button("show Github actions example", on_click=switch_click, args=["github_action"])
   if st.session_state["github_action"]:
      st.code("""
   name: Code Scanning

   on:
   push:
      branches:
         - main
         - RomKra-patch-1
   pull_request:
      branches:
         - main

   jobs:
   code-scanning:
      runs-on: ubuntu-latest

      steps:
         - name: Checkout Repository
         uses: actions/checkout@v4

         - name: Set up Python
         uses: actions/setup-python@v5
         with:
            python-version: '3.x'

         - name: Install Poetry
         uses: snok/install-poetry@v1

         - name: Install Dependencies
         run: |
            poetry install

         - name: Run pylint
         run: |
            poetry run pylint code_scanners_examples/bad_linting.py --output-format=parseable > pylint_report.txt
         continue-on-error: true

         - name: Run radon
         run: |
            poetry run radon cc code_scanners_examples/bad_complexity.py --json > radon_report.json
         continue-on-error: true

         - name: Export Requirements
         run: |
            poetry export --format requirements.txt --output requirements.txt

         - name: Run safety
         run: |
            poetry run safety check -r requirements.txt --json > safety_report.json
         continue-on-error: true

         - name: Upload Reports
         uses: actions/upload-artifact@v4
         with:
            name: code-reports
            path: |
               pylint_report.txt
               radon_report.json
               safety_report.json

   """, language="bash")

   st.markdown("""
   #### Publish your Code on PyPi

   PyPi has a really low requirement to publish, which is great to have as many contributors as possible. But this makes it easier for bad actors, active ones or not.

   We are all good, moral people

   => We would only publish packages that are as safe, clean and reliable as possible

   => We need to hold ourselves to a very high standard and enforce it for ourselves before publishing packages for others

   """)
       

with tab2: # integrate"lockfiles", "hashes", "dependency trees"
   st.subheader("Intro Supply Chain Security")
   col1, col2 = st.columns(2)
   with col1:
      criteria = ['including python','support package types','necessary packages only', 
                  "get dep tree", "uninstall packages", "lockfile",
                  "handling dep conflickst", "Installing from where"]
      conda_traits = ["yes as package", "many", "no", 
                      "two commands", "package + some additional ones","possible conda-lock",
                       "automated installation diff version", "Anaconda"]
      poetry_traits = ["no, seperate install needed", "Python only", "yes", 
                       "one command", "package + all additional ones", "automated",
                        "error message need to control yourself", "PyPi"]
      df_compare= pd.DataFrame.from_records({" ": criteria, "conda": conda_traits, "poetry(+pip)": poetry_traits})
      st.table(df_compare)
      # can combine them -> quite some articels on that topic.
      st.image("./pages/scripts/assets/env.png")

      # pypi vs conda forge about package repositories
      criteria = ['Open source Python libraries','Other open source tools','Windows/Linux/macOS packages']
      conda_forge_traits = ["many", "many", "almost always"]
      pypi_traits = ["almost all", "None", "up to maintainer (usually yes)"]
      df_compare_pck_repos = pd.DataFrame.from_records({" ": criteria, "conda-forge": conda_forge_traits, "PyPi": pypi_traits})
      st.table(df_compare_pck_repos)
      # missing text

# bsp criteria für tabelle -> conda vs poetry
# including python? -> yes as package vs no
# support package types -> many vs only python
# necessary packages only -> no vs yes
# get dep tree -> two commands vs one command
# uninstall packages -> package + some additional ones vs package + all additional ones
# lockfile -> possible conda-lock vs automatically
# handling dep conflickst automated installation diff version vs stop + error message (resolve yourself)
# perfromance both have different issues

# add pypi vs conda-forge


#easy-to-read minimal configuration file

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
    
    
   
with tab5:
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
            - conda can create sort of an environment file in the yaml format to distribute to others using also conda. Create it using: 
               - conda list --explicit --export --md5 > environment.yml
            - and then create a new environment with
               - conda create -n <name> -f environment.yaml
            - now you can share the yaml-file with everyone. If you only want to adapt to updates you need the following command:
               - conda update --file environment.yml 
            - you can alternatively actually use pip inside of conda and have access to many of pips features (although it can make it own problems)
            - Condas biggest selling point is its large usage in scientific computing and AI. The big community with this focus uses conda and develops it with this use case in mind.
         there are others: like hatch, pdm, rye.. not time to go into all. 
            What we can do: Use lockfiles because version pins, 
         this can f.e. mitigate squat attacks, avoids dependency confusion. 
         

            """)
with tab6:
   st.write(""" hashes
            Hashes verify the file downloaded from PyPI is the same as the version uploaded to PyPI hash computed when uploaded 
            verifies no manipulation/change 

            """)  

with tab7:
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

with tab8:
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
