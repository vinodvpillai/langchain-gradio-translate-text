import gradio as gr

def greet(name, age):
    return f"Hello {name}, your age is {int(age)}?"

# 1. Default UI components
demo = gr.Interface (
    fn=greet,
    inputs=["text","slider"],
    outputs=["text"]
)

# 2. Custom UI components
demo1 = gr.Interface (
    fn=greet,
    inputs=[gr.Textbox(placeholder="Name"),"slider"],
    outputs=gr.Textbox(placeholder="Result", show_label=True)
)

#demo.launch()

# Gradio lets you easily share a machine learning demo without having to worry about the hassle of hosting on a web server.
# Simply set share=True in launch()
demo1.launch(share=True)

# Run the application
# python main.py

# Gradio app in hot reload mode, which automatically reloads the Gradio app whenever you make changes to the file
# gradio app.py 