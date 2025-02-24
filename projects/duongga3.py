from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from io import BytesIO
from pathlib import Path

file_name = "BLACK_2XL_SCJISX9JD_B_1-1_left_MATRIXTEAM_SHIRT_GILDAN_01132025" + ".pdf"
old = r"E:\work\pet_project\img"
new = r"E:\work\pet_project\jpeg"


def draw_circle_on_existing_pdf(
    input_pdf, output_pdf, x, y_from_top, radius, page_number=0
):
    # Read the input PDF
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Get page dimensions
    page = reader.pages[page_number]
    page_width = float(page.mediabox.width)
    page_height = float(page.mediabox.height)

    # Calculate Y-coordinate from bottom-left
    y = page_height - y_from_top

    # Create an overlay PDF with the green circle
    overlay = BytesIO()
    c = canvas.Canvas(overlay, pagesize=(page_width, page_height))

    # Draw the green circle
    c.setFillColorRGB(0, 1, 0)  # RGB for green
    c.circle(x, y, radius, stroke=0, fill=1)
    c.save()

    # Add the overlay to the original PDF
    overlay.seek(0)
    overlay_pdf = PdfReader(overlay)

    # Merge the overlay with the target page
    for i, page in enumerate(reader.pages):
        if i == page_number:
            page.merge_page(overlay_pdf.pages[0])
        writer.add_page(page)

    # Write the modified PDF to the output
    with open(output_pdf, "wb") as f:
        writer.write(f)


# Example Usage
draw_circle_on_existing_pdf(
    input_pdf=Path(old, file_name),
    output_pdf=Path(new, file_name),
    x=700,  # 500 points from the left
    y_from_top=100,
    radius=36,  # Radius of the circle
    page_number=0,  # Modify the first page
)
