import streamlit as st

tab1, tab2, tab3, tab4, tab5, tab6  = st.tabs(["coding security", "vulnerabilities", "path traversal", "code injection", "typosquatting", "attacking"])

with tab1:
    st.write("### structure of chapter:")
    st.write("""
             checklist style (überarbeiten)
    2. Coding practices (evt in analogie oder ableitung aus it security?) -> similar to updates on your system -> keep python version and dependencies up to date \n
    
    - code analysis, \n
    - input validation \n
    - dependency vulnerabilities \n
    - other \n
    - other \n
    """)

with tab2:
        st.write("""
             what are vulnerabilities and exploits 
             3. Python specific: \n
             What are the threats and what can I do?
             - list of threats to adress
             1. path traversal
             2. code injection
             ...
             - how can you go about it """)


with tab3:

    st.write("""
     CVE-2023-51449\n
    """)
    sample_python_code = """
    import gradio as gr
    
    demo_img = "./images/skull-and-crossbones.png"
    
    def show_image(img):
        return img
    
    app = gr.Interface(
        fn=show_image,
        inputs=gr.Image(label="Input Image Component", value=demo_img, height=800, width=800),
        outputs=[gr.Image(label="Output Image Component", height=400, width=400, image_mode="L")]
    )
    
    app.launch(share=True)
    """
    st.code(sample_python_code)
    
    code = st_ace(
        value=sample_python_code,
        language='python', 
        theme='tomorrow_night',
        tab_size= 4,
        font_size=16, height=200
    )
    
    eval(code)

#
#
## code editor config variables
#height = [19, 22]
#language="python"
#theme="default"
#shortcuts="vscode"
#focus=False
#wrap=True
#editor_btns = [{
#    "name": "Run",
#    "feather": "Play",
#    "primary": True,
#    "hasText": True,
#    "showWithIcon": True,
#    "commands": ["submit"],
#    "style": {"bottom": "0.44rem", "right": "0.4rem"}
#  }]

#
## code editor
##response_dict = code_editor(sample_python_code,  height = height, lang=language, theme=theme, shortcuts=shortcuts, focus=focus, buttons=editor_btns, options={"wrap": wrap})
##import streamlit as st
##from streamlit_ace import st_ace
##
##
##code = st_ace(
##    value=sample_python_code,
##    language='python', 
##    theme='tomorrow_night',
##    tab_size= 4,
##    font_size=16, height=200
##)
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
