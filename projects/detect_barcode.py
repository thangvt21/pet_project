import re
from pathlib import Path

import numpy as np
from pdf2image import convert_from_path
import cv2
from pyzbar.pyzbar import decode

BASEDIR = Path(__file__).resolve().parent
images = cv2.imread(r"D:\work\pet_project\img\576754350712853068.png")
gray_img = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
# images = convert_from_path(
#     BASEDIR.parent / "img" / "1729653851-dp-4742b6ae131ccda5e603c0c6b2778e80.pdf"
# )

# images = [np.array(i)[:, :, ::-1] for i in images]
# images = [np.array(i)[:, :, ::-1] for i in img]
# for nr, image in enumerate(images):
#     gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

barcode = decode(gray_img)
print(barcode)
# data_barcode = barcode[0].data
# result = re.search(r"(?<=\x1d)\d+", data_barcode.decode())
# print(result.group())
# cv2.imshow("aa", gray_img)
# cv2.waitKey(0)
