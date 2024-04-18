# Create a custom Streamlit component to capture stdout and stderr
class StreamlitOutputRedirector:
    def __init__(self, placeholder):
        self.buffer = ""
        self.placeholder = placeholder

    def write(self, text):
        # Define a keyword to selectively redirect
        #keyword_to_redirect = "frames/s]"
        #
        ## Check if the keyword is present in the text
        #if keyword_to_redirect in text:
        #    # Redirect text containing the keyword to Streamlit
        #    # sys.__stdout__.write(text) # Testing
        #
        #    # Split the input string at each "|"
        #    split_elements = text.split("|")
        #    left  = split_elements[0].strip() # contains percentage complete
        #    right = split_elements[2].strip() # contains "frames/s" information
        #    newText = left + " | " + right
        #    # self.setText(newText)
        #    self.buffer += newText
        #else:
        #    # Print text without the keyword to the console
        sys.__stdout__.write(text)

    def flush(self):
        # Display the captured output
        self.placeholder.write(f"###### {self.buffer}") # markdown, write very small
        self.buffer = ""  

    def clear(self):
        # Clear the Streamlit screen by emptying the placeholder
        self.placeholder.empty()

    def setText(self, newText):
        # Write content into placeholder
        # self.placeholder.write(newText) # normal writing
        self.placeholder.write(f"###### {newText}") # markdown, write very small

    def replacePlaceholder(self, newPlaceholder):
         # Replace with the desired placeholder, which may not be initially known
         self.placeholder = newPlaceholder

# Create an empty placeholder for dynamic content
output_placeholder = st.empty()

# Create an instance of the custom StreamlitOutputRedirector
output_redirector = StreamlitOutputRedirector(output_placeholder)

# Redirect stdout and stderr to the custom redirector
sys.stdout = output_redirector
sys.stderr = output_redirector

#def transcribeAudio():
#    progress = st.sidebar.empty()                   # Create the desired placeholder for progress information
#    output_redirector.replacePlaceholder(progress)  # Replace the existing placeholder
#    output_redirector.setText("0% complete")        # Set the initial text
#    results = model.transcribe(tempTargetPath, fp16=False, word_timestamps = True, verbose=False) 
#   
#   # ***The progress bar will now automatically capture and update the "progress" place holder***


import gradio as gr

demo_img = "./assets/skull-and-crossbones.png"

def show_image(img):
    return img

app = gr.Interface(
    fn=show_image,
    inputs=gr.Image(label="Input Image Component", value=demo_img, height=800, width=800),
    outputs=[gr.Image(label="Output Image Component", height=400, width=400, image_mode="L")]
)
def transcribeAudio():
    progress = st.sidebar.empty()                   # Create the desired placeholder for progress information
    output_redirector.replacePlaceholder(progress)  # Replace the existing placeholder
    output_redirector.setText("0% complete") 
    app.launch(share=True)