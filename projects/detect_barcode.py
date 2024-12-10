from pathlib import Path
from flask import Flask
from PIL import Image
from pdf2image import convert_from_path
import pytesseract as tess
import os
import re


app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
PATH_IMAGE = r"D:\work\pet_project\jpeg"
tess.pytesseract.tesseract_cmd = str(BASE_DIR / "Tesseract-OCR" / "tesseract.exe")

pattern1 = r"TRK# (\d{4} \d{4} \d{4})"
pattern2 = r"ID# (\d{4} \d{4} \d{4})"
TRACKING_22 = r"\d{4} \d{4} \d{4} \d{4} \d{4} \d{2}"
TRACKING_26 = r"\d{4} \d{4} \d{4} \d{4} \d{4} \d{4} \d{2}"

pattern_fedex = [pattern1, pattern2]
pattern_usps = [TRACKING_22, TRACKING_26]
provider = ["Pitney Bowes", "FedEx", "UPS"]
pattern_ups = r"1Z [A-Z0-9]{3} [A-Z0-9]{3} [A-Z0-9]{2} [A-Z0-9]{4} [A-Z0-9]{4}"


def check_label():
    res = {}
    for _, _, files in os.walk(PATH_IMAGE):
        for file in files:
            file_path = os.path.join(PATH_IMAGE, file)
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"No such file or directory: '{file_path}'")
            if file.endswith(".pdf"):
                images = convert_from_path(file_path)
                text = ""
                for image in images:
                    text += tess.image_to_string(image) + "\n"
            else:
                text += tess.image_to_string(Image.open(file_path)) + "\n"
            print(text)

            # for p in provider:
            #     match2 = re.search(p, text)

            #     if match2:
            #         match = re.search(pattern_ups, text)
            #         print(p)
            #         if match:
            #             print(match.group())

            # label = ""
            # tracking = ""
            # for pr in provider:
            #     if re.search(pr, text):
            #         label = pr
            #         if label == "FedEx":
            #             for pa in pattern_fedex:
            #                 match = re.search(pa, text)
            #                 if match:
            #                     tracking = match.group(1)
            #         else:
            #             for pa in pattern_usps:
            #                 match = re.search(pa, text)
            #                 if match:
            #                     tracking = match.group()
            #         break
            # res[file] = {
            #     "label": label,
            #     "tracking": tracking,
            # }
            # print(res)


check_label()
