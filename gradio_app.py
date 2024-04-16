import gradio as gr

demo_img = "./pages/scripts/assets/skull-and-crossbones.png"

def show_image(img):
    return img

app = gr.Interface(
    fn=show_image,
    inputs=gr.Image(label="Input Image Component", value=demo_img, height=800, width=800),
    outputs=[gr.Image(label="Output Image Component", height=400, width=400, image_mode="L")]
)

app.launch(share=True)