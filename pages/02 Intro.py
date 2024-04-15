
import streamlit as st


tab1, tab2, tab3  = st.tabs(["why care?","story", "practice"])

with tab1:
    st.write("### intro slide:")
    
    st.write("""
             how many of you have crypto wallets?
    How many heard about the typosquatting attack beginning of march?  \n
    How many have pip installed some of these library in the last year? \n
    How many of you do typos? \n
    -> expect every hand to go up actually \n """)

with tab2:
    st.write("""
            Cartoon image:
            There are some people earn money by tricking others on the internet:
            actors in the internet mostly interested in your money 
             -> part of a company maby in internal workings of your company 
             -> higher position in your account and priveleges that come with them in order to get 
             to company digital assets and leverage them again for money \n 
             - ergänzug xz als beispiel
             """)
    st.write("""
            -> different attacks +  social engineering \n
            -> they use common human behaviour to their advantage \n
            -> reason why you should care a bit about security
             """)

with tab3:
    st.write("""
            -> overview relevant security aspects \n
            -> practical examples of what code can do to python applications  \n
            -> practices and tools to strengthen your applciations \n
             3 images (heaven/hell/fighter)
             """)             
             
# look into: IT-Security principles in general, coding principles apply to python, python specific practices \n

    
