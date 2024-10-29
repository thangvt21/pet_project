import re
from codecs import ignore_errors
from pathlib import Path

import cv2
from pyzbar.pyzbar import decode, ZBarSymbol

BASEDIR = Path(__file__).resolve().parent
images = cv2.imread(r"D:\work\pet_project\img\AJNZOCS3W_3181355_shipment_label.png")
gray_img = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
# images = convert_from_path(
#     BASEDIR.parent / "img" / "1729653851-dp-4742b6ae131ccda5e603c0c6b2778e80.pdf"
# )

# images = [np.array(i)[:, :, ::-1] for i in images]
# images = [np.array(i)[:, :, ::-1] for i in img]
# for nr, image in enumerate(images):
#     gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

barcode = decode(gray_img,symbols=[ZBarSymbol.CODE128])
result = re.search(r'(\d{12})$', barcode[0].data.decode())
print(result.group())


# print(barcode)
# data_barcode = barcode[0].data
# result = re.search(r"(?<=\x1d)\d+", data_barcode.decode())
# print(result.group())
# cv2.imshow("aa", gray_img)
# cv2.waitKey(0)
