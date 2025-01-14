import datetime
import os
import shutil

today = datetime.datetime.now()

DROPBOX_PATH = r"D:\FlashPOD Dropbox"
BACKUP_PATH = DROPBOX_PATH + r"\BackupFlashPOD"
FLASHPOD_PATH = DROPBOX_PATH + r"\FlashPOD"
FOLDER_DIR = str(today.year) + "_" + str(today.month)

# ---------------Nhập tên folder muốn chuyển----------------------
FOLDER_NAME = "2024_12_12"
# ----------------------------------------------------------------


# app.get("/move_folder/{folder_name}")
for machine in range(1, 43):  # Machine 1 to 42
    machine_name = "Machine " + str(machine)
    src_path = os.path.join(FLASHPOD_PATH, machine_name, FOLDER_DIR)
    des_path = os.path.join(BACKUP_PATH, machine_name)
    try:
        print(os.path.join(src_path, FOLDER_NAME))
        # shutil.move(os.path.join(src_path, FOLDER_NAME), des_path)
        # shutil.rmtree(os.path.join(src_path, FOLDER_NAME))
    except Exception as e:
        print(e)
