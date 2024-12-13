import datetime
import os
import shutil
import csv
from pathlib import Path

today = datetime.datetime.now()
folder_today = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
backup_path = r"D:\FlashPOD Dropbox\BackupFlashPOD"

# Import CSV files of order_code, folder_name, folder_type
# Folder_names
with open(r"D:\work\pet_project\img\folder.csv", "r") as file:
    data = csv.reader(file)
    list_folders = []
    for row in data:
        list_folders.append(row)
flat_list_folders = [item[0] for item in list_folders]

# Order_codes
with open(r"D:\work\pet_project\img\list.csv", "r") as file:
    data2 = csv.reader(file)
    list_codes = []
    for row in data2:
        list_codes.append(row)
flat_list_codes = [item[0] for item in list_codes]

# Folder types
with open(r"D:\work\pet_project\img\des.csv", "r") as file:
    data3 = csv.reader(file)
    list_types = []
    for row in data3:
        list_types.append(row)
flat_list_types = [item[0] for item in list_types]

# Create folder in BackupFlashPOD
for folder_type in flat_list_types:
    set_des = Path(backup_path, folder_today, folder_type)
    set_des.mkdir(parents=True, exist_ok=True)
    # print(set_des)

# Find filename and move to BackupFlashPOD
count = 0
src_list = []
for f in flat_list_folders:
    local_path = Path("D:/", f)
    for dirpaths, dirnames, files in os.walk(local_path):
        for file in files:
            full_path = Path(dirpaths) / file
            filename = full_path.name
            folder = full_path.parts[5]
            # machine = full_path.parts[3]
            for order_code in flat_list_codes:
                if order_code in filename:
                    src_path = Path(local_path, filename)
                    count += 1
                    for type_name in flat_list_types:
                        if type_name in folder:
                            folder = type_name
                        # print(type_name)
                        # print(folder)
                    des_path = Path(backup_path, folder_today, folder, filename)
                    # print(src_path, des_path)
                    shutil.move(src_path, des_path)
# print(des_path)
# print(count)
