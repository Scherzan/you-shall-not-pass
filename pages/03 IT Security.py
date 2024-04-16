import streamlit as st

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Basics","IT security principles", "Cyber Security", "dos and don'ts", "passwords"])

with tab1:
    st.write("### structure of chapter:")
    # https://www.security.org/digital-safety/cyber-security-tips/#:~:text=Don't%20click%20on%20unfamiliar,Fi%20networks%20without%20a%20VPN.
    # integrate at some point: Personally Identifiable Information phishing
    # quelle basics it security verhalten: https://www.bsi.bund.de/EN/Themen/Verbraucherinnen-und-Verbraucher/Informationen-und-Empfehlungen/Cyber-Sicherheitsempfehlungen/cyber-sicherheitsempfehlungen_node.html
    st.write("""
       word cloud of begriffe oben + wichtigsten hervorheben?   Begrifffe bsp aus erstem link   
    1. IT-Security general advice most familiar with \n

    - update your software \n
    - practice Password Hygiene \n
    - when possible (and practical) add 2FA \n 
    - use Antivirus Software \n
    - activate little hidden (because standard) Firewall \n
    """)

with tab2: # https://www.explainxkcd.com/wiki/index.php/2176:_How_Hacking_Works # https://www.explainxkcd.com/wiki/index.php/792:_Password_Reuse
    # a lot not all at once -> overwhelming maby do nothing most of you do this already to some extend
    # understand principles guide focus on aspects relevant to you and your work 
    # key point here go through theory (understadn the field and the way to interact with it)
    st.write(""" It security principles what we aim for? 
             - CIA Triad
             animated slide -> cia (officer) -> lupe zu schlagzeilen, integrits viz? (meme), A shoutout open source community
             - """)
# inofficial -> what is the field about -> conclude out of official labels CIA traid ? make link = understand
# official principles to follow = basic thing to follow
# There are three basic principles of information security:

#Confidentiality
#Integrity
#Availability
#Together, these principles are known as the CIA Triad. Every infosec program must follow these principles for maximum effectiveness.
#common model that forms the basis for the development of security systems (information security)
# 
Confidentiality ensures that sensitive information is accessed only by authorized individuals.
Integrity, the focus of our project, involves maintaining the accuracy and consistency of data across its lifecycle, ensuring that it is not altered or tampered with by unauthorized parties.
Availability ensures that information and resources are accessible to authorized users when needed.
thoughts: C -> don't upload your private keys -> schlagzeile einblenden
I -> use lockfiles and hashes -> go into deeper later
A -> it is to everyone all the time = open source

with tab3:
    
    st.write("""add to characteristics of cyber security environment
(mindset and topics)
             fiel chracteristics and directions to interact with it\n
             - everything is broken software and internet is not safe
             - ...""")


with tab4:
    st.write(""" dos and don'ts
    behaviours expressed in emojis (serious ones)
    - exercise caution (don't click on suspicious things/ downloads/pii entering) \n
                          - email entering
             - check get hacked?
    - browse with care (browser settings, https websites (an in the middle attack: don't worry about someone getting in between us and PyPI) \n
    - check get hacked 
    ... many more \n  
    """)

with tab5:
    st.write("Again on passwords -> how its cracked -> show python function")
    st.write("How to crack a password")
    st.write(""" brute force vs logic (types of exploits from course) 
                 -> look at one closer: passwords -> why need to be long -> \n
             ...\n
    
    it security course -> reference where you have the info from: \n
    
    - crack a password -> showcase how long it takes \n""") # use content of info sec course

# xz social engineering -> multi layer attack..
