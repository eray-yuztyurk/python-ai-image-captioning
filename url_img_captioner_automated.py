

# import libraries
import requests
from urllib.parse import urljoin
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
from transformers import AutoProcessor, BlipForConditionalGeneration

# loading processor and model
auto_processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# define URL and get website content
url = "https://en.wikipedia.org/wiki/Vienna"

header = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=header)
print("Status:", response.status_code, "HTML size:", len(response.text))

soup = BeautifulSoup(response.text, "html.parser")
img_tags = soup.find_all("img")
print(f"Found {len(img_tags)} <img> tags")

# write path and caption in a txt file
with open("img_captions.txt", "w", encoding="utf-8") as img_captions:
    for img_no, img in enumerate(img_tags, start=1):

        # get url for each img tag
        url_img = img.get("src") or img.get("data-src")

        # check if not "src or "data-src" is given but "srcset"
        if not url_img:
            srcset = img.get("srcset")
            if srcset:
                url_img = srcset.split()[0]

        # skip if none of them is available
        if not url_img:
            continue

        # also skip SVGs
        if ".svg" in url_img:
            continue

        # correct relative urls
        if url_img.startswith("//"):
            url_img = "https:" + url_img
        else:
            url_img = urljoin(response.url, url_img)

        if not url_img.startswith("http"):
            continue
    
        try:
            # get image from url_img and convert PIL Image after applying BytesIO
            response_img = requests.get(url_img, timeout=10, headers=header)
            img_from_bytes = Image.open(BytesIO(response_img.content))

            # eliminate images under 100 pixels as they are too small to get caption
            w, h = img_from_bytes.size
            if w < 100 or h < 100:
                continue

            # convert to required format for processor
            img_for_processor = img_from_bytes.convert("RGB")

            # get input image by appling AutoProcessor
            input_img = auto_processor(images=img_for_processor, text="This is an image of ", return_tensors="pt")

            # get output from model
            output_img = model.generate(**input_img, max_length=100)

            # decode output using Auto Processor to get caption
            img_caption = auto_processor.decode(output_img[0], skip_special_tokens=True)

            img_captions.write(f"{url_img}: {img_caption}\n")
            print(f"Caption #{img_no} saved")

        except OSError:
            continue

        except Exception as e:
            print(f"Error by Caption #{img_no}")
            continue
