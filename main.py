import gradio as gr
from gradio.themes.utils import colors, fonts, sizes

def greet(name):
    return "Hello " + name + "!"

def calc(num1, op_add, op_sub, op_multi, op_divide, num2):
    if op_add:
        return num1 + num2
    if op_sub:
        return num1 - num2
    if op_multi:
        return num1 * num2
    if op_divide:
        if num2 == 0:
            raise gr.Error("Cannot divide by zero!")
        return num1 / num2

zeph = gr.Interface(fn=calc,inputs=["number","checkbox","checkbox","checkbox","checkbox","number"],outputs="number",title="Zeph's Gradio Calculator",clear_btn="clear",
                    submit_btn="SUBMIT",allow_flagging="never", theme=gr.themes.Soft(text_size=gr.themes.sizes.text_lg))

with gr.Blocks(theme=gr.themes.Soft(),css=".gradio-container {padding: 80%}") as zeph2:
    Num1 = gr.Number(label="Num1")

    with gr.Row():
        op_add = gr.Checkbox(label="+")
        op_sub = gr.Checkbox(label="-")
        op_multi = gr.Checkbox(label="*")
        op_divide = gr.Checkbox(label="/")

    Num2 = gr.Number(label="Num2")

    with gr.Column():
        sub_button = gr.Button("Submit", variant="secondary")
        clear_button = gr.Button("Clear")

    result = gr.Text(label="Results")

    sub_button.click(
        fn=calc,
        inputs=[Num1, op_add, op_sub, op_multi, op_divide, Num2],
        outputs=result
    )

    clear_button.click(
        fn=lambda: "",
        inputs=[],
        outputs=result
    )

demo = gr.Interface(fn=greet,
                    inputs=gr.Textbox(lines = 10, placeholder="Enter your input here...."), outputs=gr.Textbox(lines = 2,value=""),)

zeph2.launch()
#gr.themes.builder()

