import os
import pygsheets
import pandas as pd
import openpyxl

root = r"D:\FlashPOD Dropbox\FlashPOD\Machine 2\2025_1\2025_1_7\01_24H_0107_P2_SET_HOODIE_GILDAN_8"
excel_file_name = "test"
folder_path = "D:\\work\\pet_project\\img\\"


def split_by_underline(file):
    name, _ = os.path.splitext(file)
    name = name.replace("-", "_")
    transform_str = name.split("_")
    split = [s.strip() for s in transform_str]
    return split


class Order:
    def __init__(
        self,
        date,
        order_code,
        side1,
        size,
        color,
        set_number,
        set_order,
        side2,
        seller,
        product_type,
        provider,
    ):
        self.color = color
        self.size = size
        self.order_code = order_code
        self.side1 = side1
        self.set_number = set_number
        self.set = set_order
        self.side2 = side2
        self.seller = seller
        self.product_type = product_type
        self.provider = provider
        self.date = date


def create_order_single(file):
    split = split_by_underline(file)
    order = Order(
        split[0],
        split[1],
        split[2],
        split[3],
        split[4],
        split[5],
        split[6],
        split[7],
        split[8],
        split[9],
        split[10],
    )
    return order


def create_order_set(file):
    split = split_by_underline(file)
    order = Order(
        split[2],
        split[1],
        split[0],
        split[3],
        split[4],
        split[5],
        split[6],
        split[7],
        split[8],
        split[9],
        split[10],
    )
    return order


def get_file_name(order):
    variant = (
        # order.date
        # + "_"
        order.order_code
        # + "_"
        # + order.seller
        # + "_"
        # + order.product_type
        # + "_"
        # + order.color
        # + "_"
        # + order.size
        # + "_"
        # + order.set_number
        # + "_"
        # + order.set
        # + "_"
        # + order.side1
    )
    return variant


def connect_to_sheet(json_dir, spread_sheets_id, sheet_name):
    gc = pygsheets.authorize(service_account_file=json_dir)
    spreadsheet = gc.open_by_key(spread_sheets_id)
    worksheet = spreadsheet.worksheet_by_title(sheet_name)
    return worksheet


def get_pdf_list(path):
    lst_single = []
    lst_set = []
    for _, _, files in os.walk(path):
        for file in files:
            if file.endswith(".pdf"):
                split = split_by_underline(file)
                if split[3] != "1":
                    # order = create_order_set(file)
                    # file_name = get_file_name(order)
                    file_name = split[0]
                    lst_set.append(file_name)
                else:
                    # order = create_order_single(file)
                    # file_name = get_file_name(order)
                    # lst_single.append(file_name)
                    file_name = split[2]
                    lst_single.append(file_name)
    return lst_single, lst_set


def main():
    order_set_all = get_pdf_list(root)[0]
    order_set = list(dict.fromkeys(order_set_all))
    order_single_all = get_pdf_list(root)[1]
    order_single = list(dict.fromkeys(order_single_all))

    df1 = pd.DataFrame(order_set)
    df2 = pd.DataFrame(order_single)

    sheets = {"Sheet1": df1, "Sheet2": df2}
    # print(sheets)
    with pd.ExcelWriter(
        folder_path + excel_file_name + ".xlsx",
        engine="openpyxl",
    ) as writer:
        for name, df in sheets.items():
            df.to_excel(writer, sheet_name=name, index=False)
            print("Excel file with " + name + " created successfully!")


main()
