# Image Text Extractor

This project is an example of a program generated using the gpt-engineer. It is a Python script that extracts text from all images in a specified directory and saves the extracted text to TXT files. The filenames of the TXT files correspond to the image files. This script uses the Tesseract library.

## Environment

This script is designed to run on a Windows 10 operating system. The Tesseract OCR engine should be installed in `C:\Program Files\Tesseract-OCR`, and the Chinese language pack should be located in `C:\Program Files\Tesseract-OCR\tessdata`.

## Dependencies

- Tesseract OCR engine: You can download and install it from [here](https://github.com/UB-Mannheim/tesseract/wiki).
- Chinese language pack for Tesseract: You can download it from [here](https://github.com/tesseract-ocr/tessdata).

## How to Use

1. Clone this repository to your local machine.
2. Install the Tesseract OCR engine and the Chinese language pack as described in the Dependencies section.
3. Run the Python script, specifying the directory containing the images as an argument.
4. The script will extract the text from the images and save it to TXT files in the same directory.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Thanks to the Tesseract team for their OCR engine and language packs.
- Thanks to the gpt-engineer for generating this program.