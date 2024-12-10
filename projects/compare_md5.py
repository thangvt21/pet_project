import hashlib


def calculate_md5(file_path):
    """Calculate the MD5 hash of a file."""
    with open(file_path, "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()


def compare_images(image1_path, image2_path):
    """Compare two images by their MD5 hashes."""
    md5_1 = calculate_md5(image1_path)
    md5_2 = calculate_md5(image2_path)

    if md5_1 == md5_2:
        print("The images are identical.")
    else:
        print("The images are different.")
    print(f"MD5 of Image 1: {md5_1}")
    print(f"MD5 of Image 2: {md5_2}")


# Example usage:
image1 = r"D:\work\pet_project\img\531054.png"
image2 = r"D:\work\pet_project\img\1729572785574.png"

compare_images(image1, image2)
