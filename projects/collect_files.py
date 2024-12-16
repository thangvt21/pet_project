import datetime
import os
import shutil
import csv
from pathlib import Path

today = datetime.datetime.now()
# folder_today = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
folder_before = "before15"
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
    set_des = Path(backup_path, folder_before, folder_type)
    # set_des = Path(backup_path, folder_today, folder_type)
    set_des.mkdir(parents=True, exist_ok=True)
# print(set_des)

# Find filename and move to BackupFlashPOD
count = 0
src_list = []
des_list = []

for f in flat_list_folders:
    local_path = Path("D:/", f)
    for dirpaths, dirnames, files in os.walk(local_path):
        for file in files:
            full_path = Path(dirpaths) / file
            filename = full_path.name
            folder = full_path.parts[6]
            # machine = full_path.parts[3]
            check = 0
            for order_code in flat_list_codes:
                if order_code in filename:
                    src_path = Path(local_path, filename)
                    if src_path not in src_list:
                        src_list.append(src_path)
                        check = 1
                    for type_name in flat_list_types:
                        if type_name in folder:
                            folder = type_name
                            des_path = Path(
                                backup_path, folder_before, folder, filename
                            )  # for folder before today
                            # des_path = Path(
                            #     backup_path, folder_today, folder, filename
                            # )  # folder today
                            # print(des_path)
                    if des_path not in des_list:
                        des_list.append(des_path)
            count += check
# print(count)

# len_src = len(src_list)
# len_des = len(des_list)
# print(len_des, len_src)
if len(src_list) != len(des_list):
    raise ValueError("Source and destination lists must have the same length.")
c = 0
for src, des in zip(src_list, des_list):
    # print(src, des)
    try:
        shutil.move(src, des)
    except Exception as e:
        print("Error", e)
    c += 1
print(c)
