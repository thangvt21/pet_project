import mimetypes
import re
from pathlib import Path
from urllib.parse import urlparse

import cv2
import numpy as np
import pygsheets
import requests
from pdf2image import convert_from_path
import pyzbar.pyzbar
import pyzbar.wrapper

BASE_DIR = Path(__file__).resolve().parent

SHEET_ID = "1lX8xs3zJVinhRs_r4itv6V8gAw4Aut8rY_waj3LHql4"
JSON_PATH = BASE_DIR.parent / "luminous-lodge-321503-c17157d58b87.json"
IMAGE_PATH = BASE_DIR.parent / "img"


def detect_link_and_transform(url: str):
    download_link = ""
    ggdrive_link_pattern = (
        r"(https?://drive\.google\.com/(?:file/d/|open\?id=)([a-zA-Z0-9_-]+))"
    )
    matches = re.findall(ggdrive_link_pattern, url)
    if not matches:
        return url
    else:
        for _, url in matches:
            file_id = url.split("id=")[-1]
            download_link = f"https://drive.google.com/uc?export=download&id={file_id}"
        return download_link


def get_filename_from_headers(response):
    # Try to extract filename from the 'Content-Disposition' header
    content_disposition = response.headers.get("Content-Disposition")
    if content_disposition:
        parts = content_disposition.split(";")
        for part in parts:
            if "filename=" in part:
                return part.split("=", 1)[1].strip('"')

    # Fallback to extracting the file extension from the 'Content-Type' header
    content_type = response.headers.get("Content-Type")
    if content_type:
        ext = mimetypes.guess_extension(content_type.split(";")[0].strip())
        if ext:
            return f"downloaded_file{ext}"
    return None


def get_filename_from_url(url):
    # Extract the filename from the URL if present
    parsed_url = urlparse(url)
    return parsed_url.path.split("/")[-1] if "/" in parsed_url.path else None


def get_worksheet_from_ggsheet(sheet_id: str, file_json: str):
    sheet_name = input("Tên sheet: ")
    gc = pygsheets.authorize(service_account_file=file_json)
    spreadsheet = gc.open_by_key(sheet_id)
    worksheet = spreadsheet.worksheet_by_title(sheet_name.strip())
    return worksheet


def detect_usps_barcode(filepath: str):
    gray = ""
    if filepath.endswith(".pdf"):
        images = convert_from_path(filepath)
        images = [np.array(i)[:, :, ::-1] for i in images]
        for nr, image in enumerate(images):
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        images = cv2.imread(filepath)
        gray = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
    barcode = pyzbar.decode(gray, symbols=[pyzbar.ZBarSymbol.CODE128])
    data_barcode = barcode[0].data
    usps = re.search(r"(?<=\x1d)\d+", data_barcode.decode())
    return usps.group()


def detect_fedex_barcode(filepath: str):
    gray = ""
    if filepath.endswith(".pdf"):
        images = convert_from_path(filepath)
        images = [np.array(i)[:, :, ::-1] for i in images]
        for nr, image in enumerate(images):
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        images = cv2.imread(filepath)
        gray = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
    barcode = pyzbar.decode(gray, symbols=[pyzbar.ZBarSymbol.CODE128])
    try:
        fedex = re.search(r"(\d{12})$", barcode[1].data.decode())
        return fedex.group()
    except ValueError:
        fedex = re.search(r"(\d{12})$", barcode[0].data.decode())
        return fedex.group()


def download_images(url: str):
    if url:
        # Download PDF, Images from url that get from Google Sheet:
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            filename = get_filename_from_headers(response) or get_filename_from_url(url)
            filepath = f"{IMAGE_PATH}/{filename}"
            with open(filepath, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
        return filepath


def main():
    worksheet = get_worksheet_from_ggsheet(SHEET_ID, str(JSON_PATH))
    worksheet_data = worksheet.get_all_values(
        returnas="matrix",
        majdim="rows",
        include_tailing_empty=False,
        include_tailing_empty_rows=False,
    )
    for i, data_sheet in enumerate(worksheet_data, start=1):
        if data_sheet:
            url = detect_link_and_transform(data_sheet[3])
            try:
                if url:
                    filepath = download_images(url)
                    try:
                        data = detect_usps_barcode(filepath)
                    except ValueError:
                        data = detect_fedex_barcode(filepath)
                    value = str(data).replace(" ", "")
                    worksheet.update_value(f"E{i}", value, parse=True)
                else:
                    value = "Lỗi link label"
                    worksheet.update_value(f"E{i}", value, parse=True)
                    # Update the cell's background color
                    worksheet.apply_format(
                        f"E{i}:E{i}",
                        {"backgroundColor": {"red": 1, "green": 0, "blue": 0}},
                    )
                    continue
            except Exception as e:
                print("Skipping empty link", e)


main()
