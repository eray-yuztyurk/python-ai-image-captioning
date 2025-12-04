
# importing libraries
import gradio as gr
import numpy as np
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

auto_processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def get_image_caption(img_input: np.ndarray):
    # converting np array to PIL image and RBG
    img = Image.fromarray(img_input).convert("RGB")

    # processing uploaded image
    input_img = auto_processor(images=img, text="This is an image of ", return_tensors="pt")
    '''
    _input example

    {
    'pixel_values': tensor([[[[ ... ]]]]),       # image → normalized float32 pixel tensor
    'input_ids': tensor([[ 133,  567,  98,  12]]),  # "the image of" → token IDs
    'attention_mask': tensor([[1, 1, 1, 1]])
    }
    '''

    # generating caption for uploaded image
    output_img = model.generate(**input_img, max_length=100)
    '''
    _output example

    tensor([[ 1012,  2234,  567,  98,  33,  2021,   12]])
    '''

    # decoding output tokens into text
    decoded_caption = auto_processor.decode(output_img[0], skip_special_tokens=True)

    return decoded_caption

_ui = gr.Interface(
    fn=get_image_caption,
    inputs=gr.Image(),
    outputs="text",
    title="What is it on that image?",
    description="Simple web application for image captioning using BLIP pretrained model"
)

_ui.launch()