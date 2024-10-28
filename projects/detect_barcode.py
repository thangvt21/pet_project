import re
import numpy as np
from pdf2image import convert_from_path
import cv2
from pyzbar.pyzbar import decode

# img = cv2.imread(r"D:\work\pet_project\img\8JPKY7FLT_566282_shipment_label.png")

images = convert_from_path(
    r"D:\work\pet_project\img\8JPKY7FLT_566282_shipment_label.png"
)

images = [np.array(i)[:, :, ::-1] for i in images]
# images = [np.array(i)[:, :, ::-1] for i in img]
for nr, image in enumerate(images):
    gray = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)

barco = decode(gray)
print(barco)
# data_barcode = barco[0].data
# result = re.search(r"(?<=\x1d)\d+", data_barcode.decode())
# print(result.group())
# cv2.imshow("aa", gray)
# cv2.waitKey(0)
