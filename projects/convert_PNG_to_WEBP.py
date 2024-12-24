from PIL import Image

# Open the PNG file
input_image = r"D:\work\pet_project\img\download (1).png"
output_image = r"D:\work\pet_project\img\2.webp"

image = Image.open(input_image)
# Save as WebP with lossless option
image.save(output_image, "WEBP", lossless=True)

print(f"Converted {input_image} to {output_image}")
