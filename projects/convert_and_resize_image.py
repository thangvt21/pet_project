import os
from PIL import Image
import threading
from pathlib import Path

input_folder = r"D:\work\pet_project\img"
output_folder = r"D:\work\pet_project\jpeg"

def convert_and_resize_images(input_folder, output_folder, max_width, max_height):
    for dirpath, _, filenames in os.walk(input_folder):
        relative_path = Path(dirpath, input_folder)
        output_path = Path(output_folder, relative_path)
        os.makedirs(output_path, exist_ok=True)
        for filename in filenames:
            if filename.lower().endswith(".png"):
                input_file_path = os.path.join(dirpath, filename)
                output_file_path = os.path.join(output_path,
                                                os.path.splitext(filename)[0] + f"{max_width}x{max_height}" + ".jpeg")
                try:
                    with Image.open(input_file_path) as img:
                        rgb_img = img.convert("RGB")
                        rgb_img.thumbnail((max_width, max_height))
                        rgb_img.save(output_file_path, format="JPEG", quality=85)
                        print(
                            f"Converted and resized: {input_file_path} -> {output_file_path}"
                        )
                except Exception as e:
                    print(f"Error processing {input_file_path}: {e}")


# Example usage


if __name__ == "__main__":
    # max_width = int(input("Width: "))  # 592 #82 #278
    # max_height = int(input("Height: "))  # 592 #82 #278

    size1 = threading.Thread(
        target=convert_and_resize_images, args=(input_folder, output_folder, 200, 200)
    )
    size2 = threading.Thread(
        target=convert_and_resize_images, args=(input_folder, output_folder, 800, 800)
    )
    # size3 = threading.Thread(
    #     target=convert_and_resize_images, args=(input_folder, output_folder, 278, 278)
    # )
    size1.start()
    size2.start()
    # size3.start()
    size1.join()
    size2.join()
    # size3.join()
    print("Xong")
