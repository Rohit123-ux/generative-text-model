import gradio as gr
from transformers import pipeline, set_seed

generator = pipeline("text-generation", model="gpt2")
set_seed(42)

def generate_text(prompt):
    result = generator(prompt, max_length=100, num_return_sequences=1)
    return result[0]['generated_text']

interface = gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(lines=2, placeholder="Enter a topic..."),
    outputs="text",
    title="AI Text Generator"
)

interface.launch()