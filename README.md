# Python AI Image Captioning

This project provides a practical set of tools for generating captions for images using the BLIP model. You can caption images by uploading a single file, processing all images in a local folder, or scraping images from a webpage. The interface is simple and user-friendly, making it easy for anyone to use.

## Features

- **Single Image Upload:** Instantly get a caption for any image you upload via the web interface.
- **Bulk Local Captioning:** Automatically process all images in a folder and save their captions to a file.
- **Webpage Scraping:** Find and caption all images from any webpage you provide.
- **Easy Web Interface:** All tools use Gradio-based web UIs for convenience.
- **Docker Support:** Run the whole project easily in a container.

## Screenshots

**Single Image Upload:**
<img width="2490" height="1218" alt="image" src="https://github.com/user-attachments/assets/f5897b32-4aca-439b-a9b8-cb371ff371e8" />
**Bulk Local Captioning:**
<img width="2478" height="844" alt="image" src="https://github.com/user-attachments/assets/ec5b10fe-0d10-45f4-903f-8b6eb27c2824" />
**Webpage Scraping:**
<img width="2486" height="672" alt="image" src="https://github.com/user-attachments/assets/e65df0df-321d-442f-b3fe-6ff3c784a559" />

## Installation

1. **Clone the repository:**
	 ```bash
	 git clone https://github.com/eray-yuztyurk/python-ai-image-captioning.git
	 cd python-ai-image-captioning/python-ai-image-captioning-1
	 ```

2. **Make sure Python 3.10+ is installed.**

3. **Create and activate a virtual environment:**
	 ```bash
	 python3.10 -m venv venv
	 source venv/bin/activate
	 ```

4. **Install dependencies:**
	 ```bash
	 pip install --upgrade pip
	 pip install -r requirements.txt
	 ```

## Usage

### Start All Interfaces Together

```bash
python3.10 main.py
```
Each interface will open on its own port (7860, 7861, 7862). If your browser does not open automatically, visit these addresses manually.

### Run Individual Scripts

- **Single image upload:**  
	`python3.10 uploaded_image_captioner.py`  
	(Port: 7860)

- **Local folder images:**  
	`python3.10 local_img_captioner_automated.py`  
	(Port: 7862)

- **Webpage scraping:**  
	`python3.10 url_img_captioner_automated.py`  
	(Port: 7861)

### Run with Docker

```bash
docker build -t ai-image-captioning .
docker run -p 7860:7860 -p 7861:7861 -p 7862:7862 ai-image-captioning
```

## Example Output

```
cat.jpg: a small orange cat sitting on a windowsill
https://example.com/image1.png: a group of people standing in front of a building
```

## Notes

- Make sure the `outputs/` directory exists, or specify a valid output path.
- The BLIP model will be downloaded automatically on first run.
- For best results, use clear and sufficiently large images (at least 100x100 pixels).

## Contributing & License

This project is released under the MIT License. If you want to contribute, feel free to open an issue or pull request.

## Acknowledgements

- [Salesforce BLIP](https://github.com/salesforce/BLIP)
- [Gradio](https://gradio.app/)
- [HuggingFace Transformers](https://huggingface.co/docs/transformers/index)
# Python AI Image Captioning App

This repository contains a set of simple, practical tools for generating captions for images using the BLIP (Bootstrapped Language Image Pretraining) model. You can use these tools to caption images from your local folders, from a web page, or by uploading a single image through a web interface.

## Features

- **Single Image Captioning:** Upload an image and instantly get a descriptive caption.
- **Bulk Local Captioning:** Automatically generate captions for all images in a local folder.
- **Webpage Scraping & Captioning:** Scrape all images from a given webpage and generate captions for each.

All tools use the open-source BLIP model from Salesforce, ensuring high-quality, context-aware captions.

---

## Installation

1. **Clone the repository:**
	```bash
	git clone https://github.com/eray-yuztyurk/python-ai-image-captioning.git
	cd python-ai-image-captioning/python-ai-image-captioning-1
	```

2. **Install Python 3.10+** (required for Gradio 5.x and latest Transformers).

3. **Create and activate a virtual environment:**
	```bash
	python3.10 -m venv venv
	source venv/bin/activate
	```

4. **Install dependencies:**
	```bash
	pip install --upgrade pip
	pip install -r requirements.txt
	```

---

## Usage

### 1. Caption a Single Uploaded Image

Run:
```bash
python3.10 uploaded_image_captioner.py
```
- Opens a Gradio web interface.
- Upload an image and get a caption instantly.

---

### 2. Caption All Images in a Local Folder

Run:
```bash
python3.10 local_img_captioner_automated.py
```
- Enter the path to your image folder, file extensions (e.g. `jpg,jpeg,png`), and output file path.
- The script will process all images and save captions to a text file.

---

### 3. Scrape and Caption Images from a Webpage

Run:
```bash
python3.10 url_img_captioner_automated.py
```
- Enter a webpage URL and an output file path in the Gradio interface.
- The script will download all images from the page, generate captions, and save them.

---

## Example Output

The output is a simple text file with lines like:
```
cat.jpg: a small orange cat sitting on a windowsill
https://example.com/image1.png: a group of people standing in front of a building
```

---

## Notes

- Make sure the `outputs/` directory exists, or specify a valid output path.
- The BLIP model will be downloaded automatically on first run (requires internet).
- For best results, use clear and sufficiently large images (at least 100x100 pixels).

---

## License

This project is open-source and uses only open-source models and libraries.

---

## Acknowledgements

- [Salesforce BLIP](https://github.com/salesforce/BLIP)
- [Gradio](https://gradio.app/)
- [HuggingFace Transformers](https://huggingface.co/docs/transformers/index)

---

Feel free to open issues or contribute improvements!
