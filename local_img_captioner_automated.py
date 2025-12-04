

# import libraries
import glob
from PIL import Image
import io
from transformers import AutoProcessor, BlipForConditionalGeneration

# loading processor and model
auto_processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# define path and image types
image_directory = "/path/to/your/images"
image_extentions = ["jpg", "jpeg", "png"]

# write path and caption in a txt file
with open("local_img_captions.txt", "w") as img_captions:
    
    for img_ext in image_extentions:
        for img_dir in glob.glob(os.path.join(image_directory, f"*.{img_ext}"))

        # convert PIL Image and required format for processor
        img_for_processor = Image.open(img_dir).convert("RGB")

        # get input image by appling AutoProcessor
        input_img = auto_processor(images=img_for_processor, text="This is an image of ", return_tensors="pt")

        # get output from model
        output_img = model.generate(**input_img, max_length=100)

        # decode output using Auto Processor to get caption
        img_caption = auto_processor.decode(output_img[0], skip_special_tokens=True)

        img_captions.write(f"{os.path.basename(img_dir)}: {img_caption}\n")

