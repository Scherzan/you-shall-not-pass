
import streamlit as st


tab1, tab2, tab3  = st.tabs(["are you involved?","yes if you are human", "what to do?"])



with tab1:
    if "step" not in st.session_state:
        st.session_state['step'] = 'Q0'
    if "question" not in st.session_state:
        st.session_state['question'] = "Who has a crypto wallet?"
    # A function to easily go from one step to another
    def change_step(next_step):
        st.session_state['step'] = next_step
    
    # Let's initialize our session state
    if st.session_state['step'] == "Q0":
        st.session_state['question'] = "Who has a crypto wallet?"
        st.button("❓🙋", on_click=change_step, args=["Q1"])
    
    # Step 1
    if st.session_state['step'] == "Q1":
        st.session_state['question'] = "Who heard of the Typosquatting attack beginning of march?"
        st.button("❓🙋", on_click=change_step, args=["Q2"])
    
    # Step 2
    if st.session_state['step'] == "Q2":
        st.session_state['question'] = "Who uses pip install directly in the terminal?"
        st.button("❓🙋", on_click=change_step, args=["Q3"])
    
    # Step 3
    if st.session_state['step'] == "Q3":
        st.session_state['question'] = "Who does typos?"
        st.button("❓🙋", on_click=change_step, args=["Q0"])


    # We print our data everytime
    st.write(st.session_state['question'])


with tab2:
    st.image("./pages/scripts/assets/how_hacking_works.png")
            #Cartoon image:
            #There are some people earn money by tricking others on the internet:
            #actors in the internet mostly interested in your money 
            # -> part of a company maby in internal workings of your company 
            # -> higher position in your account and priveleges that come with them in order to get 
            # to company digital assets and leverage them again for money \n 

    st.write("""
            -> most often atack vector combined with social engineering \n
            -> they use common human behaviour to their advantage \n
            -> reason why you should care a bit about security
             """)
# human behaviour = make typos
# if you have some personal information and behave like a human > susceptible to hacking activity
with tab3:
    st.image("./pages/scripts/assets/heaven_hell_footsteps.png") # anpassung navigate securly and compromised systems and data
    #st.write("""
    #        -> overview relevant security aspects \n
    #        -> practical examples of what code can do to python applications  \n
    #        -> practices and tools to strengthen your applciations \n
    #         """)             

#1. How is it supposed to work?  heaven
#2. What can go wrong? hell
#3. how to we mitigate risk of it going wrong? footsteps      
# look into: IT-Security principles in general, coding principles apply to python, python specific practices \n

    
