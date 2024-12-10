from pathlib import Path

from flask import Flask
from PIL import Image

from pdf2image import convert_from_path
import pytesseract as tess
import os
import re


app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
PATH_IMAGE = r"D:\work\pet_project\img"
tess.pytesseract.tesseract_cmd = str(BASE_DIR / "Tesseract-OCR" / "tesseract.exe")

fedex_TRK = r"TRK# (\d{4} \d{4} \d{4})"
fedex_ID = r"ID# (\d{4} \d{4} \d{4})"
usps_22 = r"\d{4} \d{4} \d{4} \d{4} \d{4} \d{2}"
usps_26 = r"\d{4} \d{4} \d{4} \d{4} \d{4} \d{4} \d{2}"
ups_1Z = r"1Z [A-Z0-9]{3} [A-Z0-9]{3} [A-Z0-9]{2} [A-Z0-9]{4} [A-Z0-9]{4}"

tracking_fedex = [fedex_TRK, fedex_ID]
tracking_usps = [usps_22, usps_26]

providers = ["Pitney Bowes", "FedEx", "UPS"]


@app.get("/check_label")
def check_label():
    res = {}
    for _, _, files in os.walk(PATH_IMAGE):
        for file in files:
            file_path = os.path.join(PATH_IMAGE, file)
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"No such file or directory: '{file_path}'")

            text = ""
            if file.endswith(".pdf"):
                images = convert_from_path(file_path)
                for image in images:
                    text += tess.image_to_string(image) + "\n"
            else:
                text += tess.image_to_string(Image.open(file_path)) + "\n"

            tracking = ""
            label = ""
            for pr in providers:
                if re.search(pr, text):
                    label = pr
                    if label == "Pitney Bowes":
                        for pa in tracking_usps:
                            match = re.search(pa, text)
                            if match:
                                tracking = match.group()
                    elif label == "FedEx":
                        for pa in tracking_fedex:
                            match = re.search(pa, text)
                            if match:
                                tracking = match.group(1)
                    else:
                        match = re.search(ups_1Z, text)
                        if match:
                            tracking = match.group()
                else:
                    match = re.search(ups_1Z, text)
                    if match:
                        tracking = match.group()
            res[file] = {
                "label": label or "UPS",
                "tracking": tracking or "Not Found",
            }
    return res
