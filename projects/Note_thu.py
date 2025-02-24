import datetime
import os
from pathlib import Path
from PyPDF2 import PdfMerger
from pdfCropMargins import crop

today = datetime.datetime.now()
folder_name = str(today.day) + "_" + str(today.month)
# Specify the folder containing PDF files

current_dir = os.getcwd()

pdf_folder = Path(current_dir, "PDF")


def mergePDF(pdf_folder, folder_name):
    # Initialize PdfMerger
    merger = PdfMerger()

    # List all PDF files in the folder and sort them (optional)
    pdf_files = sorted([f for f in os.listdir(pdf_folder) if f.endswith(".pdf")])

    # Loop through and append each PDF
    for pdf in pdf_files:
        full_path = os.path.join(pdf_folder, pdf)
        merger.append(full_path)

    # Save the merged PDF
    output_file = os.path.join(current_dir, f"{folder_name}.pdf")
    merger.write(output_file)
    merger.close()
    crop_args = [
        "-o",
        os.path.join(current_dir, f"{folder_name}_vt21.pdf"),  # Output file
        "-p",
        "5",  # Optional: Percent margin to retain (default is 10%)
        os.path.join(current_dir, f"{folder_name}.pdf"),  # Input file
    ]

    crop(crop_args)


mergePDF(pdf_folder, folder_name)
