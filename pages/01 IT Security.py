import streamlit as st
import subprocess

st.set_page_config(
    layout="wide",
)

st.markdown(
    """
<style>
.big-font {
    font-size:30px !important;
}
</style>
""",
    unsafe_allow_html=True,
)

tab1, tab2, tab3, tab4 = st.tabs(
    ["Cyber Security", "IT Security", "Passwords", "Data Health Check"]
)

with tab1:
    st.header("Hacking Humans")
    st.write("""                 
        🔃 update your software \n
        🔐 practice password hygiene \n
        📱 when possible add 2FA \n 
        😷 use Antivirus Software \n
        🧱 keep active Firewall \n
        📧 don't open files and links in phising mail 
        """)

    st.code("pip install amtplotlib # installing matplotlib")

    with st.popover("Enter"):
        st.image("./pages/assets/recent_typosquatting.png")


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
        st.image("./pages/assets/CIA-triad.png")

    with col2:
        st.image("./pages/assets/git_leackage.png")


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
    st.header("Carefull development process for small scale applications.")
    with st.expander("Scetch the idea (Design)"):
        st.image("./pages/assets/password_process.png")
    with st.expander("Implement the scetch (Implementation)"):
        show_code = st.checkbox("Show password_app.py content")

        if show_code:
            code_to_pw = """
            import time
            
            RETREIVED_REAL_PASSWORD = "1234"
            
            def check_password(password): 
                
                if len(password) != len(RETREIVED_REAL_PASSWORD):
                    return False
                for x, y in zip(password, RETREIVED_REAL_PASSWORD):
                    time.sleep(0.05)
                    if int(x) != int(y):
                        return False
                return True
            
            # check_password() is equal to 'if password == RETREIVED_REAL_PASSWORD'
            ...
            """
            st.code(code_to_pw)
            # This means that comparing two strings can take differing amounts of time when depending on the location of the first difference

        def run_py_script(script_name):
            command = ["python", "-u", script_name]
            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )
            while process.poll() is None:
                line = process.stdout.readline()
                if not line:
                    continue
                st.write(line.strip())

        # When the user submits the script name, run the shell script
        if st.button("Run password_app.py"):
            run_py_script("password_app.py")

    with st.expander("Try to break through your code (Verification)."):
        show_code = st.checkbox("Show crack_password.py content")

        if show_code:
            code_to_pw = """

            ...
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
            ...
                    
            """
            st.code(code_to_pw)

        def run_py_script(script_name):
            command = ["python", "-u", script_name]
            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )
            while process.poll() is None:
                line = process.stdout.readline()
                if not line:
                    continue
                st.write(line.strip())

        # When the user submits the script name, run the shell script
        if st.button("Run crack_password.py"):
            run_py_script("crack_password.py")
        st.write("#")
        st.write("#")
        st.write("#")
        st.write(
            "* Find a full example on how to hack a python web application coded in Flask at: https://sqreen.github.io/DevelopersSecurityBestPractices/timing-attack/python"
        )

with tab4:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Toolbox Data Health Check:")
        check_credentials = st.checkbox(
            "Check credential leakage with: https://haveibeenpwned.com/"
        )
        check_pw = st.checkbox(
            "Check new passwords against password lists: https://password.kaspersky.com/"
        )
        if check_pw:
            st.write("Many password managers have this kind of check built in.")
        secret_check = st.checkbox(
            "Check for leaked secrets: https://www.gitguardian.com/hasmysecretleaked"
        )
        frequent_use = st.checkbox(
            "make password easy to remember and hard to guess (combine 4 random words)"
        )
    with col2:
        st.image("./pages/assets/password_strength.png")
