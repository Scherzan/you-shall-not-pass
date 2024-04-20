import streamlit as st
import subprocess
from streamlit_ace import st_ace

tab1, tab2, tab3, tab4 = st.tabs(["Cyber Security","IT Security", "Passwords", "Checklist Password Hygene"])

# schema to follow:
#1. How is it supposed to work?  
#2. What can go wrong?
#3. how to we mitigate risk of it going wrong?

# we start with reviewing the basics to build on
# Unfortunately security starts with the our flaws. We all share common habits, that are leveraged to trick us
# and probably the hardest part is keep reminding ourselves on this.  
# We all adobt common cyber security tools and hope they do a decent job to protect us
# and then we code away typing pip install package

with tab1:
    st.subheader("Hacking Humans")
    # https://www.security.org/digital-safety/cyber-security-tips/#:~:text=Don't%20click%20on%20unfamiliar,Fi%20networks%20without%20a%20VPN.
    # integrate at some point: Personally Identifiable Information phishing
    # quelle basics it security verhalten: https://www.bsi.bund.de/EN/Themen/Verbraucherinnen-und-Verbraucher/Informationen-und-Empfehlungen/Cyber-Sicherheitsempfehlungen/cyber-sicherheitsempfehlungen_node.html
    col1, col2 = st.columns(2)
    with col1:
        st.image("./pages/scripts/assets/how_hacking_works.png")
    
    with col2:
        st.write("""                 
        🔃 update your software \n
        🔐 practice password hygiene \n
        📱 when possible add 2FA \n 
        😷 use Antivirus Software \n
        🧱  keep active Firewall \n
        """)

    st.code("pip install amtplotlib # installing matplotlib")

    with st.popover("Enter"):
        st.image("./pages/scripts/assets/typo_squatting.png")
        
        

# another one maby less familiar basic concept cia triad but we wil act the same
# know confidentiality is important -> for those who don't know 
# conf = sensitive information is accessed only by authorized individuals
# integrity = accuracy and consistency of data across lifecycle be sure no one unauthorized changed it
# availability = you have acces to your information when you need to
# its clear these are important -> but then might push something to git -< and ups my token is still in there
# who hasend hardcoded copy pasted access tokens into their code base before -> out of conviniece.

with tab2: 
    st.subheader("Personal Information and Humans.")
    col1, col2 = st.columns(2)

    with col1:
        col_space_left1, col_content1, col_space_right1 = st.columns((3, 8, 2))
        with col_content1:
            if st.button("Confidentiality"):
                with col2:
                    st.image("./pages/scripts/assets/git_leackage.png")
        col_space_left2, col_content2, col_space_right2 = st.columns((3, 4, 3))
        with col_content2:
            st.write("CIA-Triad")
        cola, colb = st.columns(2)
        with cola:
            if st.button("Integrity"):
                with col2:
                    st.write("hashes news")                
        with colb:
            if st.button("Availability"):
                with col2:
                    st.write("permission denied")


# Now we know we are the flaws, what to do? -> Get started with a simple Secure Software Development Lifecycle
# use example of password authentification even though much is moving direction of 2FA
# infact starting this year pypi now requires 2fa for new users (and top 1% package accounts) -> so things evolve in a good direction

# Let's say we have an application, that uses personal information: -> application to collect and prioritize social media notifications
# you will need to establish user accounts for each new user:
# requirement: -> users need accounts to use the app with their information + security need to make sure only see their own account -> pw authentification 
# design -> login to account + need to authenticate person (registration (registration phase) + authentification phase)
# development ()
# 

with tab3:
    st.header("Applying a Minimal Secure Software Development Process")
    with st.expander("Design"):
        st.image("./pages/scripts/assets/pw_process.png")
    with st.expander("Implementation"):
        show_code = st.checkbox("Show password_app.py content")

        if show_code:
            
            code_to_pw = """
            import time
            import tkinter
            from tkinter import messagebox
            
            retreived_real_password = "12345"
            
            def check_password(password): # Don't change it
                if len(password) != len(retreived_real_password):
                    return False
                for x, y in zip(password, retreived_real_password):
                    time.sleep(0.1) # Simulates the wait time of the safe's mechanism
                    if int(x) != int(y):
                        return False
                return True
            
            window = tkinter.Tk()
            window.title("Password Authentification")
            window.geometry("340x440")
            window.configure(bg="#333333")
            
            def login():
            
                if check_password(password_entry.get()):
                    messagebox.showinfo(title="Login Success", message="You entered the correct password.")
                else:
                    messagebox.showerror(title="Error", message="Invalid password.")
            
            frame = tkinter.Frame(bg='#333333')
            ...
            """
            st.code(code_to_pw)

        def run_py_script(script_name):

             command = ["python", '-u', script_name]
             process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
             while process.poll() is None:
                line = process.stdout.readline()
                if not line:
                    continue
                st.write(line.strip())
    
        # When the user submits the script name, run the shell script
        if st.button('Run password_app.py'):
            run_py_script("password_app.py")

    with st.expander("Verification"):
        show_code = st.checkbox("Show crack_password.py content")

        if show_code:
            
            code_to_pw = """
            ...
            # 1. Brute force:
            def brute_force_random():
                possible_combinations = int("".join(np.repeat(str(9), len(real_password)).tolist()))
                for pw_candidate in np.arange(0, possible_combinations, dtype=int).tolist():
                    if not check_password(str(pw_candidate)):
                        continue
                    else:
                        return str(pw_candidate)

            # 2. Timing Attack:
            def timimng_attack():
                pw_candidate = ["0","0","0","0"]
                check_time = 0.052
                for position_dig in range(4):
                    for dig in np.arange(0, 10, dtype=int).tolist():
                        pw_candidate[position_dig] = str(dig)
            
                        start = time.time()
                        if check_password("".join(pw_candidate)):
                            return "".join(pw_candidate) 
                        time_taken = time.time() - start
            
                        if time_taken > check_time:
                            check_time = check_time + 0.05
                            break
                            

            # 3. Use a password list
            with open('10k-most-common.txt', 'r') as file:
                data = file.read()
            data_into_list = data.split("\n") 
            
            def brute_force_list():
                for pw_candidate in data_into_list:
                    if not check_password(pw_candidate):
                        continue
                    else:
                        return str(pw_candidate)
                    
            """
            st.code(code_to_pw)

        def run_py_script(script_name):

             command = ["python", '-u', script_name]
             process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
             while process.poll() is None:
                line = process.stdout.readline()
                if not line:
                    continue
                st.write(line.strip())
    
        # When the user submits the script name, run the shell script
        if st.button('Run crack_password.py'):
            run_py_script("crack_password.py")        
 
with tab4:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("password hygiene")
        default = st.checkbox('change default passwords')
        different_pw = st.checkbox('use different passwords for each account')
        long_and_unique = st.checkbox('create long and unique passwords')
        if long_and_unique:
            st.write("not on any password list")
    
        st.subheader("tools and tricks to help")
        check_pw = st.checkbox('check password leakage lists and https://haveibeenpwned.com/')
        # make a poll?
        pw_manager = st.checkbox('let a password manager store passwords')
        frequent_use = st.checkbox('make password easy to remember and hard to guess (combine 4 random words)')
    with col2:
        st.image("./pages/scripts/assets/password_strength.png")    
    