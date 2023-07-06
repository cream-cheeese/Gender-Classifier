
import gradio as gr
from fastai.vision.all import *

def webcam(image):
    # Use the trained model to predict the gender of the input image
    learn = load_learner('model.pkl') 
    gender, _, probs = learn.predict(PILImage.create(image))
    processed_output = (f"This is a: {gender}.\nProbability it is a woman: {probs[1]:.4f}.\nProbability it is a man: {probs[0]:.4f}.")
    return processed_output

interface = gr.Interface(
    fn=webcam,
    inputs=[gr.Webcam()],
    outputs=[gr.Textbox(label="Results")],
)

interface.launch(share=False)