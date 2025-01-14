import os
import datetime
import pygsheets
import pandas as pd

today = datetime.datetime.now()
# FOLDER_NAME = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
# FOLDER_DIR = str(today.year) + "_" + str(today.month)

FOLDER_NAME = "2025_1_7"
FOLDER_DIR = "2025_1"

DROPBOX_PATH = "D:\\FlashPOD Dropbox\\FlashPOD\\"
JSON_PATH = (
    r"D:\work\pet_project\luminous-lodge-321503-c17157d58b87.json"
)
SHEET_ID = "1kNMeY5JrRbvocmYktfWOoWJUamW6W8AQNATDgjgtGW0"


def split_by_underline(file):
    name, _ = os.path.splitext(file)
    name = name.replace("-", "_")
    split = [s.strip() for s in name.split("_")]
    return split

def get_order_code_and_seller(path):
    list_data = []
    list_order = []
    list_seller = []
    for _, _, files in os.walk(path):
        for file in files:
            if file.endswith(".pdf"):
                split = split_by_underline(file)
                if len(split) > 7:
                    if split[4] != "1":
                        order_code = split[0]
                        seller = split[7]
                        # data = "-".join([order_code, seller])
                        if order_code not in list_data:
                            list_order.append(order_code)
                        if seller not in list_data:
                            list_seller.append(seller)
                    else:
                        order_code = split[2]
                        seller = split[7]
                        # data = " - ".join([order_code, seller])
                        if order_code not in list_data:
                            list_order.append(order_code)
                        if seller not in list_data:
                            list_seller.append(seller)
    return list_order, list_seller


def main():
    name_sheet = "Get_Order_Code"
    gc = pygsheets.authorize(service_account_file=JSON_PATH)
    spreadsheet = gc.open_by_key(SHEET_ID)
    worksheet = spreadsheet.worksheet_by_title(name_sheet)
    i = 0
    for m in range(1, 43):
        machine_path = os.path.join(
            DROPBOX_PATH, "Machine " + str(m), FOLDER_DIR, FOLDER_NAME
        )
        df, df_seller = get_order_code_and_seller(machine_path)
        data1 = pd.DataFrame(df)
        data2 = pd.DataFrame(df_seller)
        worksheet.set_dataframe(data1, start=(1,1+i), copy_head=False)
        worksheet.set_dataframe(data2, start=(1,2+i), copy_head=False)
        i += 2
main()
