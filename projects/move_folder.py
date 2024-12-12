import datetime
import os
import shutil

today = datetime.datetime.now()

DROPBOX_PATH = r"D:\FlashPOD Dropbox"
BACKUP_PATH = DROPBOX_PATH + r"\BackupFlashPOD"
FLASHPOD_PATH = DROPBOX_PATH + r"\FlashPOD"

# ---------------Nhập tên folder muốn chuyển----------------------
FOLDER_NAME = "2024_12_7"
# ----------------------------------------------------------------

FOLDER_DIR = str(today.year) + "_" + str(today.month)
MACHINE_LIST = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
]

for machine in MACHINE_LIST:
    machine_name = "Machine " + str(machine)
    src_path = os.path.join(FLASHPOD_PATH, machine_name, FOLDER_DIR)
    des_path = os.path.join(BACKUP_PATH, machine_name)
    try:
        shutil.move(os.path.join(src_path, FOLDER_NAME), des_path)
    except Exception as e:
        print(e)
    # print(os.path.join(src_path, FOLDER_NAME), des_path)
