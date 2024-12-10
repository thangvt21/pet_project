import os
from PIL import Image

# Define the input folder containing PNG files and the output folder for JPEGs
input_folder = r"D:\work\pet_project\newWeb\Catalog (ảnh sản phẩm)\Tote bag"
output_folder = r"D:\work\pet_project\outPut\Catalog (ảnh sản phẩm)\Tote bag"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".png"):  # Process only PNG files
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(
            output_folder, os.path.splitext(filename)[0] + ".jpeg"
        )

        # Open the PNG image and convert it to JPEG
        with Image.open(input_path) as img:
            rgb_img = img.convert("RGB")  # Remove alpha channel if present
            rgb_img.save(output_path, format="JPEG", quality=85)  # Save as JPEG
            print(f"Converted: {filename} -> {os.path.basename(output_path)}")

print("Conversion complete!")
