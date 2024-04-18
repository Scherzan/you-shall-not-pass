import streamlit as st

st.set_page_config(
    layout="wide",
)

if "pylint_on" not in st.session_state:
    st.session_state["pylint_on"] = False
if "radon_on" not in st.session_state:
    st.session_state["radon_on"] = False
if "safety_on" not in st.session_state:
    st.session_state["safety_on"] = False
if "Github_pipeline_on" not in st.session_state:
    st.session_state["Github_pipeline_on"] = False


def switch_click(input):
    switches = ["pylint_on", "radon_on", "safety_on", "Github_pipeline_on"]
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
- They raise the general coding hygiene, which is all the more important in a lax language like python.
- Remind you of your favorite task: Code documentation
- They help us uphold certain coding guidelines which can help make our code easier to understand. Even if the only person reading it is ourselves in 6 months! 
- Reduce Code smells
- Makes it easier to have a basic overview over dependencies and known vulnerabilities

Scanners that specialize in this use case are also known as linters. Most IDEs have linters integrated but you should make sure to adapt them to your own style.
There are many linters to choose from and there are as always debates about which is the best. But nothing is stopping you from using two or more at the same time. Some Linters that are widely used are: 
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
A different specialization got more into the complexity of your code. They warn you once your modules and classes reach a certain complexity threshold. This can be defined by different measures, like lines of code in a file/class/function or the depth of your loops and if-clauses. Examples are:
- McCabe
- Radon 
""")

st.button("Activate Radon example", on_click=switch_click, args=["radon_on"])
if st.session_state["radon_on"]:
    st.code("""
radon cc -a code_scanners_examples/bad_complexity.py

code_scanners_examples/bad_complexity.py
    F 43:0 very_high_complexity_function - C
    M 8:4 HighComplexityClass.high_complexity_method - B
    M 24:4 AnotherHighComplexityClass.another_high_complexity_method - B
    C 3:0 HighComplexityClass - B
    C 20:0 AnotherHighComplexityClass - B
    F 36:0 moderate_complexity_function - A
    M 4:4 HighComplexityClass.__init__ - A
    M 21:4 AnotherHighComplexityClass.__init__ - A

8 blocks (classes, functions, methods) analyzed.
Average complexity: B (5.75)""", language="bash")
st.markdown("""
Other Code Scanners also search for known vulnerabilities in your dependencies and other security risks. Even in a project thats only for yourself, if there is some kind of network connection involved, you want to be as secure as possible. Known security scanners are: 
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

#### Publish your Code on PyPi

PyPi has a really low requirement to publish, which is great to have as many contributors as possible. But this makes it easier for bad actors, active ones or not.

We are all good, moral people

=> We would only publish packages that are as safe, clean and reliable as possible

=> We need to hold ourselves to a very high standard and enforce it for ourselves before publishing packages for others

 """)
    