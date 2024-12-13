import datetime
import os
import shutil
import csv
from pathlib import Path

today = datetime.datetime.now()
folder_today = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
backup_path = r"D:\FlashPOD Dropbox\BackupFlashPOD"

with open(r"D:\work\pet_project\img\folder.csv", "r") as file:
    data = csv.reader(file)
    list_folder = []
    for row in data:
        list_folder.append(row)
a = [item[0] for item in list_folder]

with open(r"D:\work\pet_project\img\list.csv", "r") as file:
    data2 = csv.reader(file)
    list_code = []
    for row in data2:
        list_code.append(row)
b = [item[0] for item in list_code]

with open(r"D:\work\pet_project\img\des.csv", "r") as file:
    data3 = csv.reader(file)
    des_list = []
    for row in data3:
        des_list.append(row)
c = [item[0] for item in des_list]

for e in c:
    set_des = Path(backup_path, folder_today, e)
    set_des.mkdir(parents=True, exist_ok=True)
    # print(set_des)
count = 0
src_list = []
for f in a:
    local_path = Path("D:/", f)
    for dirpaths, dirnames, files in os.walk(local_path):
        for file in files:
            full_path = Path(dirpaths) / file
            filename = full_path.name
            folder = full_path.parts[6]
            # machine = full_path.parts[3]
            for o in b:
                if o in filename:
                    src_path = Path(local_path, filename)
                    count += 1
                    for d in c:
                        if d in folder:
                            folder = d
                    des_path = Path(backup_path, folder, filename)
                    # shutil.move(src_path, des_path)
# print(des_path)
# print(count)
