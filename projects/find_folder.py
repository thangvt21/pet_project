import datetime
import os
import shutil
import csv
from pathlib import Path

dropbox_path = r"D:\FlashPOD Dropbox\FlashPOD"

data_code = []
with open(r"D:\work\pet_project\img\list.csv", "r") as file:
    data2 = csv.reader(file)
    for row in data2:
        data_code.append(row)
list_codes = [item[0] for item in data_code]


list_path = []
count = 0
local_path = Path("D:/", dropbox_path)
for dirpaths, dirnames, files in os.walk(local_path):
    for file in files:
        full_path = Path(dirpaths) / file
        filename = full_path.name
        for order_code in list_codes:
            if order_code in filename:
                if full_path not in list_path:
                    a = str(full_path).split("\\")
                    folder = str(a[6:-1])
                    b = "_".join(folder.split("_"))
                    print(order_code, "-", b[:-1])
print(count)
