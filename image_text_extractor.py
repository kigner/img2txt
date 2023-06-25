import os
import pytesseract
from PIL import Image

class ImageTextExtractor:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'

    def extract_text_from_image(self, image_path: str) -> str:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang="chi_sim")
        return text
