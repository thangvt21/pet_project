import datetime
import os
import shutil
import csv
from pathlib import Path

today = datetime.datetime.now()
folder_created = "before21_line6"
backup_path = r"D:\FlashPOD Dropbox\BackupFlashPOD"
csv_folder = r"D:\work\pet_project\img\folder.csv"
csv_ordercode = r"D:\work\pet_project\img\order_code.csv"


def importCSV(path):
    temp = []
    with open(path, "r") as file:
        file_csv = csv.reader(file)
        for row in file_csv:
            temp.append(row)
    path_list = [item[0] for item in temp]
    return path_list


def createDestinationFolder(folder_name):
    set_des = Path(backup_path, folder_created, folder_name)
    set_des.mkdir(parents=True, exist_ok=True)


def getPathForMoveFile(order_list, folder_list):
    if len(order_list) != len(folder_list):
        raise ValueError("Check lại 2 files .csv.")
    else:
        print("order_list = folder_list => OK!")

    source_list = []
    destination_list = []

    for folder in folder_list:
        local_path = Path("D:/", folder)
        for dirpaths, _, files in os.walk(local_path):
            for file in files:
                full_path = Path(dirpaths) / file
                filename = full_path.name
                # fmt: off
                folder_name = full_path.parts[6] # D:\FlashPOD Dropbox\FlashPOD\Machine 2\2024_12\2024_12_10\<<01_24H_1210_P2_SET_HOODIE_GILDAN_27>>\.pdf
                # fmt: on
                for order_code in order_list:
                    if order_code in filename:
                        source_path = Path(local_path, filename)
                        if source_path not in source_list:
                            source_list.append(source_path)
                        # fmt: off
                        a = folder_name.split("_")          # "23","EX","1216","P12","SINGLE","SHIRT","INTHEOMOCKUP","DOILINE","1"
                        
                        if a[1] in ["24H", "EX", "O9"]:     # 23_<<EX>>_1216_P12_SINGLE_SHIRT_INTHEOMOCKUP_DOILINE_1
                            folder_name = "_".join(a[4:-1]) # 23_<<EX>>_1216_P12_<<SINGLE_SHIRT_INTHEOMOCKUP_DOILINE>>_1 
                        else:
                            folder_name = "_".join(a[3:-1]) # 23_1216_P12_<<SINGLE_SHIRT_INTHEOMOCKUP_DOILINE>>_1
                        destination_path = Path(backup_path, folder_created, folder_name, filename)
                        # fmt: on
                        if destination_path not in destination_list:
                            destination_list.append(destination_path)

                        createDestinationFolder(folder_name)
    return source_list, destination_list


def moveFile(source_list, destination_list):
    if len(source_list) != len(destination_list):
        raise ValueError("Danh sách folder gốc và folder mới không bằng nhau")
    else:
        print("Source list = Destination list => OK")
    print("Bắt đầu move files...")
    for source, destination in zip(source_list, destination_list):
        try:
            shutil.move(source, destination)
        except Exception as e:
            print("Error", e)


def main():
    folder_list = importCSV(csv_folder)
    order_list = importCSV(csv_ordercode)
    source_list, destination_list = getPathForMoveFile(order_list, folder_list)
    # print(len(source_list), len(destination_list))
    moveFile(source_list, destination_list)


main()
