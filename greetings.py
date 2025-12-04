import gradio as gr

def salute(input_name):
    return "What's up, " + input_name + "?"

trial = gr.Interface(fn=salute, inputs="text", outputs="text")

trial.launch(server_name="0.0.0.0", server_port=7860)
