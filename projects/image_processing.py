import cv2
import screeninfo

# Get screen resolution
screen = screeninfo.get_monitors()[0]
screen_width = screen.width
screen_height = screen.height

# Load an image (make sure the path is correct)
image = cv2.imread(r"D:\work\pet_project\img\victor.png")

# Check if the image is loaded properly
if image is None:
    print("Error: Unable to load image")
else:
    # Get the original dimensions of the image
    original_height, original_width = image.shape[:2]

    # Calculate the new dimensions while maintaining the aspect ratio
    # Resize based on the screen width
    scale_factor = min(screen_width / original_width, screen_height / original_height)

    # Calculate new width and height based on the scale factor
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)

    # Resize the image
    resized_image = cv2.resize(image, (new_width, new_height))

    # Display the resized image in a window named "Image"
    cv2.imshow("Image", resized_image)

    # Wait for any key to close the window
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
