import streamlit as st
from streamlit_ace import st_ace

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Basics Cyber Security","IT security principles", "deep dive passwords", "deep dive cracking passwords", "summing up dos and don'ts"])

with tab1:
    st.subheader("Recap: Basic Cyber-Security Advice")
    # https://www.security.org/digital-safety/cyber-security-tips/#:~:text=Don't%20click%20on%20unfamiliar,Fi%20networks%20without%20a%20VPN.
    # integrate at some point: Personally Identifiable Information phishing
    # quelle basics it security verhalten: https://www.bsi.bund.de/EN/Themen/Verbraucherinnen-und-Verbraucher/Informationen-und-Empfehlungen/Cyber-Sicherheitsempfehlungen/cyber-sicherheitsempfehlungen_node.html
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
                 
        🔃 update your software \n
        🔐 practice password hygiene \n
        📱 when possible add 2FA \n 
        😷 use Antivirus Software \n
        🧱  keep active Firewall \n
        """)
    with col2:
        st.write("""
                ... and know the field characteristics:
                🧬 technology constantly evolvs (and with it exploits and security)
                🎯 attack possibilities are endless everything is a target
                ... so best way to stay safe?
                educate and stay informed ℹ️
                 """)

with tab2: # https://www.explainxkcd.com/wiki/index.php/2176:_How_Hacking_Works # https://www.explainxkcd.com/wiki/index.php/792:_Password_Reuse
    # a lot not all at once -> overwhelming maby do nothing most of you do this already to some extend
    # understand principles guide focus on aspects relevant to you and your work 
    # key point here go through theory (understadn the field and the way to interact with it)
    st.write("What do we want to establish? IT-Security ")
    col1, col2 = st.columns(2)

    with col1:
        cola, colb = st.columns(2)
        with cola:
            st.image("./pages/scripts/assets/CIA-triad.png")
        with colb:
            st.button("Confidentiality")
            st.button("Integrity")
            st.button("Availability")
    with col2:
        st.write("display news related to the topics")

# inofficial -> what is the field about -> conclude out of official labels CIA traid ? make link = understand
# official principles to follow = basic thing to follow
# There are three basic principles of information security:

#Confidentiality
#Integrity
#Availability
#Together, these principles are known as the CIA Triad. Every infosec program must follow these principles for maximum effectiveness.
#common model that forms the basis for the development of security systems (information security)
# 
#Confidentiality ensures that sensitive information is accessed only by authorized individuals.
#Integrity, the focus of our project, involves maintaining the accuracy and consistency of data across its lifecycle, ensuring that it is not altered or tampered with by unauthorized parties.
#Availability ensures that information and resources are accessible to authorized users when needed.
#thoughts: C -> don't upload your private keys -> schlagzeile einblenden
#I -> use lockfiles and hashes -> go into deeper later
#A -> it is to everyone all the time = open source


#What does it mean to know abou securtity?
#Go through one very well known security measure -> password for authentification
#authentification = verify user allowed access -> come across everytime you use a system
#-> maby come across in coding when you build your own apps or function
#(Part of integrity -> passwords should not be given to others )
#
#1. How is it supposed to work?  heaven
#2. What can go wrong? hell
#3. how to we mitigate risk of it going wrong? footsteps


#1.
#password as security measure -> implement this if yu code an app with login:
#- registration phase
#- picks a password, -> sequence of characters
#- register in system (record the password) i.e. database
#- authentication pahse (on login)
#- user name and password
#system looks up the user name
#in the password database is it a macth?
#-> match login sucessfull use system
#-> not matched asked to repeat process -> zeichnung


with tab3:
    st.write("What does it mean: to know about securtity practices?")
    st.write("Simple Example: Password Authentification and Security")
    st.image("./pages/scripts/assets/pw_process.png")
    #st.write("How to crack a password")
    #st.write(""" brute force vs logic (types of exploits from course) 
    #             -> look at one closer: passwords -> why need to be long -> \n
    #         ...\n
    #
    #it security course -> reference where you have the info from: \n
    #
    #- crack a password -> showcase how long it takes \n""") # use content of info sec course
#
# xz social engineering -> multi layer attack..


#1.5. -> naively solve this problem in python:
#
#we know password -> some charcters -> need to store them and then we need to check if incoming characters is equal to the basic
#
#write simple function, which compares two arrays and returns true/false for if equal or not
#
#1. This example (taken from it security course on edx)
#
#- make sure the array lengths are equal.
#- if not exist 
#- if yes continue and
#   - iterate over them
#and check if all of their element are equal.
#- if one check fails return false
#- else return true
#
#Lets say for a 20 characters long password.
#Here's the real password.
#-> check_password function gib ein false passwords _> gibt falsch aus und wnen richtige gibt es true aus
#Anyone wants to share though on how this is flawed?

#-> brute force -> trying each combination:
#-> write function for it
#10²⁰ possible combinations over a trillion.
#
#This solution is in fact flawed
#in a very subtle way.
#
#Solution:
#What if we try guessing it
#and measure how long it took the system
#to tell us that it's wrong?
#
#We look at this function:
#-> write a crack_password function:
#-> zeige deine solution ->
#
#erkläre was timing attack ist und dann zeige deine fixed solution
#-> many examples online how to write a proper password check 
#continue with 2.

# after demo
#let's consider some basic attacks:
#- steal passwords (from target directly with keylogger (hardware/Software), when in transit, or from database of service)
#- guess passwords

with tab4:
    col1, col2 = st.columns(2)
    with col1:
        code_password = """
        real_password = "2687"
        def check_password(password):
        if len(password) != len(real_password):
            return False
        for x, y in zip(password, real_password):
            time.sleep(0.1) # Simulates the wait time of the response mechanism
            if int(x) != int(y):
                return False
        return True """
    
        content = st_ace(language='python', theme="terminal", wrap=True, value=code_password)
        if content:
            #st.subheader('Content')
            st.write(content) # find method to evaluate with pyscript!? -> go through alternatives in select box one by one
            # after evaluation there is a button clear and then this content is displayed

        if st.button('Continue'):
            with col1:
                st.image("./pages/scripts/assets/pw_process_attack.png")


    with col2:
        option = st.selectbox("Code snippets:", ('demo', 'brute force', 'attack faster', 'alternative implementation'), placeholder=" ")
        if option == "demo":
            code_snippet = """
                           import time
                           pw_candidate = "3987" # "2687"
                           start = time.time()
                           print(check_password(pw_candidate))
                           time_taken = time.time() - start
                           print(time_taken) """
            st.code(code_snippet)
        elif option == "brute force":
            code_snippet = """
                           import time
                           def crack_password_brute_force():
                               possible_combinations = int("".join(np.repeat(str(9), len(real_password)).tolist()))
                               print(possible_combinations)
                               for pw_candidate in np.arange(0, possible_combinations, dtype=int).tolist():
                                   if not check_password(str(pw_candidate)):
                                       continue
                                   else:
                                       return str(pw_candidate)

                           start = time.time()
                           print(crack_password_brute_force())
                           print(f"It took {time.time() - start} seconds and 2687 trials to crack the password")"""
            
            st.code(code_snippet)

        elif option == "attack faster":
            code_snippet = """
                           import time
                           def crack_password():
                               pw_candidate = ["0", "0", "0", "0"]
                               check_time = 0.12
                               for position_dig in range(len(pw_candidate)):
                                   for dig in np.arange(0, 10, dtype=int).tolist():
                                       pw_candidate[position_dig] = str(dig)
                                       start = time.time()
                                       check_password("".join(pw_candidate))
                                       time_taken = time.time() - start
                                       print(time_taken)
                           
                                       if time_taken > check_time:
                                           check_time = check_time + 0.1
                                           break
                                                          
                               return "".join(pw_candidate) 

                           start = time.time()
                           print(crack_password())
                           print(f"It took {time.time() - start} seconds and 23 trials to crack the password")"""
            
            st.code(code_snippet)
# continuation 3 footsteps):
#password hygene:
#- 
#- use different passwords in each account 
#- long and unique (not on any password list)
#tools to help:
#- check password leakage
#- password manager to store passwords (synchronized across devices)
#- frequently used -> easy to remember and hard to guess
#as an application designer_
#- check cookiecutter examples of implementations (using hashes, cryptographie ...)
with tab5:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("password hygiene")
        default = st.checkbox('change default passwords')
        different_pw = st.checkbox('use different passwords for each account')
        if different_pw:
            st.write("(at least the important ones)")
        long_and_unique = st.checkbox('create long and unique passwords')
        if long_and_unique:
            st.write("not on any password list")
    
        st.subheader("tools and tricks to help")
        check_pw = st.checkbox('check password leakage list: https://haveibeenpwned.com/')
        # make a poll?
        pw_manager = st.checkbox('let a password manager store passwords')
        frequent_use = st.checkbox('with frequently used accounts make password easy to remember and hard to guess')
    with col2:
        if frequent_use:
            st.image("./pages/scripts/assets/password_strength.png")    
    
    #st.write(""" dos and don'ts
    #behaviours expressed in emojis (serious ones)
    #- exercise caution (don't click on suspicious things/ downloads/pii entering) \n
    #                      - email entering
    #         - check get hacked?
    #- browse with care (browser settings, https websites (an in the middle attack: don't worry about someone getting in between us and PyPI) \n
    #- check get hacked 
    #... many more \n  
    #""")
# I got hacked: