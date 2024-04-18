import gradio as gr

demo_img = "./pages/scripts/assets/skull-and-crossbones.png"

def show_image(img, exit_text):
    if exit_text=="exit":
        app.close()
    return img


app = gr.Interface(
    fn=show_image,
    inputs=[gr.Image(label="Input Image Component", value=demo_img, height=400, width=400), gr.Textbox()],
    outputs=[gr.Image(label="Output Image Component", height=200, width=200, image_mode="L")],
    )


app.launch(share=True)
