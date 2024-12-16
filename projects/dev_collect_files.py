import datetime
import os
import shutil
import csv
from pathlib import Path

today = datetime.datetime.now()
folder_created = "before15"
backup_path = r"D:\FlashPOD Dropbox\BackupFlashPOD"

# Import CSV files of order_code, folder_name, folder_type
# Folder_names
with open(r"D:\work\pet_project\img\folder.csv", "r") as file:
    data = csv.reader(file)
    data_folder = []
    for row in data:
        data_folder.append(row)
list_folders = [item[0] for item in data_folder]

# Order_codes
with open(r"D:\work\pet_project\img\list.csv", "r") as file:
    data2 = csv.reader(file)
    data_code = []
    for row in data2:
        data_code.append(row)
list_codes = [item[0] for item in data_code]

# Find filename and move to BackupFlashPOD
src_list = []
des_list = []

for f in list_folders:
    local_path = Path("D:/", f)
    for dirpaths, dirnames, files in os.walk(local_path):
        for file in files:
            full_path = Path(dirpaths) / file
            filename = full_path.name
            folder_name = full_path.parts[6]
            # machine = full_path.parts[3]
            check = 0
            for order_code in list_codes:
                if order_code in filename:
                    src_path = Path(local_path, filename)
                    if src_path not in src_list:
                        src_list.append(src_path)
                    else:
                        print("Đường dẫn bị lặp.")
                    a = folder_name.split("_")
                    if a[1] in ["24H", "EX", "O9"]:
                        folder_name = "_".join(a[4:-1])
                    else:
                        folder_name = "_".join(a[3:-1])
                    des_path = Path(backup_path, folder_created, folder_name, filename)
                    set_des = Path(backup_path, folder_created, folder_name)
                    set_des.mkdir(parents=True, exist_ok=True)
                    if des_path not in des_list:
                        des_list.append(des_path)
                    else:
                        print("Đường dẫn bị lặp.")

if len(src_list) != len(des_list):
    raise ValueError("Danh sách folder gốc và folder mới không bằng nhau")
c = 0
for src, des in zip(src_list, des_list):
    # try:
    #     shutil.move(src, des)
    # except Exception as e:
    #     print("Error", e)
    c += 1
print(c)
