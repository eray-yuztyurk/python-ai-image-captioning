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

-------
**Bulk Local Captioning:**

<img width="2484" height="846" alt="image" src="https://github.com/user-attachments/assets/54a3c68a-6b6d-4959-b80e-ce04af137f50" />

-------
**Webpage Scraping:**

<img width="2486" height="672" alt="image" src="https://github.com/user-attachments/assets/e65df0df-321d-442f-b3fe-6ff3c784a559" />

-------

## Installation

1. **Clone the repository:**
	 ```bash
	 git clone https://github.com/eray-yuztyurk/python-ai-image-captioning.git
	 cd python-ai-image-captioning
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

Feel free to open issues or contribute improvements!
