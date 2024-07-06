import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet,
                    inputs=gr.Textbox(lines = 10, placeholder="Enter your input here...."), outputs=gr.Textbox(lines = 2,value=""),)
demo.launch()