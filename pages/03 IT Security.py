import streamlit as st

tab1, tab2, tab3, tab4 = st.tabs(["advice","IT security", "reasoning", "passwords"])

with tab1:
    st.write("### structure of chapter:")
    # https://www.security.org/digital-safety/cyber-security-tips/#:~:text=Don't%20click%20on%20unfamiliar,Fi%20networks%20without%20a%20VPN.
    # integrate at some point: Personally Identifiable Information phishing
    # quelle basics it security verhalten: https://www.bsi.bund.de/EN/Themen/Verbraucherinnen-und-Verbraucher/Informationen-und-Empfehlungen/Cyber-Sicherheitsempfehlungen/cyber-sicherheitsempfehlungen_node.html
    st.write("""
       word cloud of begriffe oben + wichtigsten hervorheben?   Begrifffe bsp aus erstem link   
    1. IT-Security general advice most familiar with \n

    - Software Updates \n
    - Password Hygiene \n
    - when possible (and practical) 2FA \n 
    - Antivirus Software \n
    - little hidden (because standard) Firewall \n
    behavioural add: \n
    - exercise caution (don't click on suspicious things/ downloads/pii entering) \n
    - browse with care (browser settings, https websites (an in the middle attack: don't worry about someone getting in between us and PyPI) \n
    ... more \n  
    """)
with tab2:
    # a lot not all at once -> overwhelming maby do nothing most of you do this already to some extend
    # understand principles guide focus on aspects relevant to you and your work 
    # key point here go through theory (understadn the field and the way to interact with it)
    st.write(""" It security principles (mindset and topics)
             fiel chracteristics and directions to interact with it\n
             - everything is broken software and internet is not safe
             - ...
             - CIA Triad
             - """)
# inofficial -> what is the field about -> conclude out of official labels CIA traid ? make link = understand
# official principles to follow = basic thing to follow
# There are three basic principles of information security:

#Confidentiality
#Integrity
#Availability
#Together, these principles are known as the CIA Triad. Every infosec program must follow these principles for maximum effectiveness.

with tab3:
    st.write("""why care?
             - stories (beispiele für lücken in software etc für warum man anfangs genannte practices machen sollte)""")

with tab4:
    st.write("How to crack a password")
    st.write(""" brute force vs logic (types of exploits from course) 
                 -> look at one closer: passwords -> why need to be long -> \n
             ...\n
    
    it security course -> reference where you have the info from: \n
    
    - crack a password -> showcase how long it takes \n""")

# xz social engineering -> multi layer attack..
