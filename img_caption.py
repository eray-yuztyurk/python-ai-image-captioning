
# importing required libraries
import requests
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Loading pretrained processor and model
auto_processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Loading an image
image_path = "img/snowboarding.png"

# converting image into RGB format
uploaded_img = Image.open(image_path).convert("RGB")

# converting image format to pt (pytorch tensors) format for BLIP processor
exp_text = "This is an image of "
_input = auto_processor(images=uploaded_img, text=exp_text, return_tensors="pt")

'''
_input example

{
  'pixel_values': tensor([[[[ ... ]]]]),       # image → normalized float32 pixel tensor
  'input_ids': tensor([[ 133,  567,  98,  12]]),  # "the image of" → token IDs
  'attention_mask': tensor([[1, 1, 1, 1]])
}
'''

# generating caption for uploaded image
_output = model.generate(**_input, max_length=50)

'''
_output example

tensor([[ 1012,  2234,  567,  98,  33,  2021,   12]])
'''
# decoding the output tokens to text
img_expl = auto_processor.decode(_output[0], skip_special_tokens=True)

print(img_expl)