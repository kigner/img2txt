import os
from image_text_extractor import ImageTextExtractor

def main():
    input_directory = "D:\\images\\prompts"
    output_directory = os.path.join(input_directory, "output")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    extractor = ImageTextExtractor()

    for file in os.listdir(input_directory):
        file_path = os.path.join(input_directory, file)
        if os.path.isfile(file_path) and file.lower().endswith(('.jpg', '.png')):
            extracted_text = extractor.extract_text(file_path)
            output_file_path = os.path.join(output_directory, f"{os.path.splitext(file)[0]}.txt")
            with open(output_file_path, "w", encoding="utf-8") as output_file:
                output_file.write(extracted_text)

if __name__ == "__main__":
    main()
