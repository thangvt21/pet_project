import os
from PIL import Image


def convert_and_resize_images_592x592(
    input_folder, output_folder, max_width=592, max_height=592
):
    """
    Walks through all subdirectories of input_folder, recreates the directory structure in output_folder,
    converts PNG images to JPEG format, and resizes them to fit within max_width and max_height.
    """
    for dirpath, _, filenames in os.walk(input_folder):
        # Calculate the relative path from the input folder
        relative_path = os.path.relpath(dirpath, input_folder)
        # Construct the corresponding output path
        output_path = os.path.join(output_folder, relative_path)
        # Create the directory in the output folder
        os.makedirs(output_path, exist_ok=True)

        # Process each file in the current directory
        for filename in filenames:
            if filename.lower().endswith(".png"):  # Process only PNG files
                input_file_path = os.path.join(dirpath, filename)
                output_file_path = os.path.join(
                    output_path, os.path.splitext(filename)[0] + "592x592.jpeg"
                )

                try:
                    # Open the PNG image
                    with Image.open(input_file_path) as img:
                        # Convert to RGB (JPEG doesn't support transparency)
                        rgb_img = img.convert("RGB")

                        # Resize the image to fit within max_width and max_height
                        rgb_img.thumbnail((max_width, max_height))

                        # Save the resized image as JPEG
                        rgb_img.save(
                            output_file_path, format="JPEG", quality=85
                        )  # Adjust quality if needed
                        print(
                            f"Converted and resized: {input_file_path} -> {output_file_path}"
                        )
                except Exception as e:
                    print(f"Error processing {input_file_path}: {e}")


def convert_and_resize_images_278x278(
    input_folder, output_folder, max_width=278, max_height=278
):
    """
    Walks through all subdirectories of input_folder, recreates the directory structure in output_folder,
    converts PNG images to JPEG format, and resizes them to fit within max_width and max_height.
    """
    for dirpath, _, filenames in os.walk(input_folder):
        # Calculate the relative path from the input folder
        relative_path = os.path.relpath(dirpath, input_folder)
        # Construct the corresponding output path
        output_path = os.path.join(output_folder, relative_path)
        # Create the directory in the output folder
        os.makedirs(output_path, exist_ok=True)

        # Process each file in the current directory
        for filename in filenames:
            if filename.lower().endswith(".png"):  # Process only PNG files
                input_file_path = os.path.join(dirpath, filename)
                output_file_path = os.path.join(
                    output_path, os.path.splitext(filename)[0] + "278x278.jpeg"
                )

                try:
                    # Open the PNG image
                    with Image.open(input_file_path) as img:
                        # Convert to RGB (JPEG doesn't support transparency)
                        rgb_img = img.convert("RGB")

                        # Resize the image to fit within max_width and max_height
                        rgb_img.thumbnail((max_width, max_height))

                        # Save the resized image as JPEG
                        rgb_img.save(
                            output_file_path, format="JPEG", quality=85
                        )  # Adjust quality if needed
                        print(
                            f"Converted and resized: {input_file_path} -> {output_file_path}"
                        )
                except Exception as e:
                    print(f"Error processing {input_file_path}: {e}")


def convert_and_resize_images_82x82(
    input_folder, output_folder, max_width=82, max_height=82
):
    """
    Walks through all subdirectories of input_folder, recreates the directory structure in output_folder,
    converts PNG images to JPEG format, and resizes them to fit within max_width and max_height.
    """
    for dirpath, _, filenames in os.walk(input_folder):
        # Calculate the relative path from the input folder
        relative_path = os.path.relpath(dirpath, input_folder)
        # Construct the corresponding output path
        output_path = os.path.join(output_folder, relative_path)
        # Create the directory in the output folder
        os.makedirs(output_path, exist_ok=True)

        # Process each file in the current directory
        for filename in filenames:
            if filename.lower().endswith(".png"):  # Process only PNG files
                input_file_path = os.path.join(dirpath, filename)
                output_file_path = os.path.join(
                    output_path, os.path.splitext(filename)[0] + "82x82.jpeg"
                )

                try:
                    # Open the PNG image
                    with Image.open(input_file_path) as img:
                        # Convert to RGB (JPEG doesn't support transparency)
                        rgb_img = img.convert("RGB")

                        # Resize the image to fit within max_width and max_height
                        rgb_img.thumbnail((max_width, max_height))

                        # Save the resized image as JPEG
                        rgb_img.save(
                            output_file_path, format="JPEG", quality=85
                        )  # Adjust quality if needed
                        print(
                            f"Converted and resized: {input_file_path} -> {output_file_path}"
                        )
                except Exception as e:
                    print(f"Error processing {input_file_path}: {e}")


# Example usage
input_folder = r"D:\work\pet_project\newWeb"
output_folder = r"D:\work\pet_project\outPut"

# Set desired max dimensions for the resized images
# max_width = int(input("Width: "))  # 592 #82 #278
# max_height = int(input("Height: "))  # 592 #82 #278

convert_and_resize_images_592x592(
    input_folder, output_folder, max_width=592, max_height=592
)
convert_and_resize_images_278x278(
    input_folder, output_folder, max_width=278, max_height=278
)
convert_and_resize_images_82x82(
    input_folder, output_folder, max_width=82, max_height=82
)

print("Image conversion, resizing, and directory structure replication complete!")
