import os
from pathlib import Path
import fitz

import pytesseract as tess
from PIL import Image
import re
import pygsheets
import requests

BASE_DIR = Path(__file__).resolve().parent

SHEET_ID = "1lX8xs3zJVinhRs_r4itv6V8gAw4Aut8rY_waj3LHql4"
JSON_PATH = BASE_DIR / "luminous-lodge-321503-2defcccdcd2d.json"
PATH_IMAGE = BASE_DIR / "img"
TESSERACT_PATH = BASE_DIR / "Tesseract-OCR" / "tesseract.exe"

# Regex of USPS tracking numbers
TRACKING_22 = r"\d{4} \d{4} \d{4} \d{4} \d{4} \d{2}"
TRACKING_26 = r"\d{4} \d{4} \d{4} \d{4} \d{4} \d{4} \d{2}"

# Regex of FEDEX tracking numbers
FEDEX2 = r"\bTRK# \d{4} \d{4} \d{4}\b"
FEDEX1 = r"\bID# \d{4} \d{4} \d{4}\b"


def connect_to_sheet(sheet_id: str):
    sheet_name = input("Tên sheet: ")
    gc = pygsheets.authorize(service_account_file=JSON_PATH)
    spreadsheet = gc.open_by_key(sheet_id)
    worksheet = spreadsheet.worksheet_by_title(sheet_name.strip())
    return worksheet


def ocr_pdf_and_match(filename: str):
    try:
        #     images = convert_from_path(filename)
        #     for i, image in enumerate(images):
        #         name = str(i) + "_" + os.path.basename(filename) + ".jpeg"
        #         image.save(
        #             PATH_IMAGE + name,
        #             "JPEG",
        #         )
        #         tess.pytesseract.tesseract_cmd = str(TESSERACT_PATH)
        #         text = tess.image_to_string(Image.open(PATH_IMAGE + name))
        #         pdf_text = "" + text
        #         transform_text = "".join(pdf_text.replace("\n", " "))
        pdf_document = fitz.open(filename)
        pdf_text = ""

        for i in range(len(pdf_document)):
            # Get the page
            page = pdf_document[i]

            # Render page to an image
            pix = page.get_pixmap()

            # Save the image as JPEG
            name = f"{i}_{os.path.basename(filename)}.jpeg"
            image_path = os.path.join(PATH_IMAGE, name)
            pix.save(image_path)

            # Open the saved image for OCR
            text = tess.image_to_string(Image.open(image_path))
            pdf_text += text + " "  # Append text with a space for separation

        # Close the PDF document
        pdf_document.close()

        # Transform the text to remove newlines
        transform_text = pdf_text.replace("\n", " ")
        match = re.search(TRACKING_26, transform_text)
        if match:
            return match.group()
        else:
            match = re.search(TRACKING_22, transform_text)
            if match:
                return match.group()
    except Exception as e:
        print(str(e))


def convert_ggdrive_link_to_download(drive_link: str):
    try:
        file_id = drive_link.split("/d/")[1].split("/")[0]
        return f"https://drive.google.com/uc?id={file_id}"
    except IndexError:
        return None


def main():
    worksheet = connect_to_sheet(SHEET_ID)
    a = worksheet.get_all_values(
        returnas="matrix",
        majdim="rows",
        include_tailing_empty=False,
        include_tailing_empty_rows=False,
    )
    for i, v in enumerate(a, start=1):
        if v:
            output_path = os.path.join(PATH_IMAGE, f"{v[0]}.pdf")
            url = convert_ggdrive_link_to_download(v[3])
            if url:
                with requests.get(url, stream=True) as r:
                    r.raise_for_status()
                    with open(output_path, "wb") as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            f.write(chunk)
                data = ocr_pdf_and_match(output_path)
                value = str(data).replace(" ", "")
                worksheet.update_value(f"E{i}", value, parse=True)


main()
