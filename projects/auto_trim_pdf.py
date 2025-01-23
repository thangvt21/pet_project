from pdfCropMargins import crop

# Define input/output files and crop margins
crop_args = [
    "-o",
    "output.pdf",  # Output file
    "-p",
    "5",  # Optional: Percent margin to retain (default is 10%)
    r"E:\work\pet_project\projects\23_1.pdf",  # Input file
]

crop(crop_args)  # Crop the PDF
