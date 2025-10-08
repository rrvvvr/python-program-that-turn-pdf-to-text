import os
import pytesseract
from PIL import Image

# Point this to your Tesseract installation
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Folder containing your cleaned PNGs
input_folder = r"C:\Users\b\Downloads\needed"
output_file = r"c:\Users\b\Downloads\pdf_series\ocr_output.txt"

with open(output_file, "w", encoding="utf-8") as out:
    for file in sorted(os.listdir(input_folder)):
        if file.lower().endswith(".png"):
            image_path = os.path.join(input_folder, file)
            print(f"OCR on: {file}")
            
            text = pytesseract.image_to_string(
                Image.open(image_path),
                lang="eng",  # English OCR
                config="--psm 6"  # Assume uniform text blocks
            )
            
            out.write(f"===== {file} =====\n")
            out.write(text.strip())
            out.write("\n\n")

print(f"OCR complete! Output saved to: {output_file}")
