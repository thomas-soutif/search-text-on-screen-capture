import cv2
import pytesseract
from PIL import Image
import numpy as np
import mss
import time

def get_screen_resolution():
    with mss.mss() as sct:
        # Get monitor 1, as mss uses 1-based indexing for monitors
        monitor = sct.monitors[1]
        return monitor["width"], monitor["height"]

# Function to capture the entire screen
def capture_screen():
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Capture the primary monitor
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)
        return img

# Function to capture a specific region of the screen
def capture_screen_region(left, top, width, height):
    with mss.mss() as sct:
        region = {'left': left, 'top': top, 'width': width, 'height': height}
        screenshot = sct.grab(region)
        img = np.array(screenshot)
        return img

def capture_top_left_screen_region():
    scale_factor=0.3
    # Get the screen resolution
    screen_width, screen_height = get_screen_resolution()

    # Calculate the coordinates of the top right region
    region_width = int(screen_width * scale_factor)
    region_height = int(screen_height * scale_factor)
    region_left = 0  # Leftmost side
    region_top = 0  # Topmost side

    # Capture the region using mss
    with mss.mss() as sct:
        region = {'left': region_left, 'top': region_top, 'width': region_width, 'height': region_height}
        screenshot = sct.grab(region)
        img = np.array(screenshot)
        return img

# Function to process the image and extract text
def process_image(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to preprocess the image
    _, binary_img = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Perform OCR
    text = pytesseract.image_to_string(binary_img)
    return text

# Function to save the image to a file
def save_image(image, filename):
    cv2.imwrite(filename, image)


################################################ --------- Main ####################################################

def main():
    words_to_find = ['site-packages', 'any_word']
    try:
        while True:
            start_time = time.time()

            screen_image = capture_top_left_screen_region()
            #save_image(screen_image, "captured_window.png")
            extracted_text = process_image(screen_image)

            end_time = time.time()
            elapsed_time = end_time - start_time

            # Print the extracted text
            print("Extracted Text:")
            print(extracted_text)
            print(f"Elapsed Time: {elapsed_time:.2f} seconds")

            for word in words_to_find:
                if word.lower() in extracted_text.lower():
                    print(f"Found stop word '{word}' in extracted text. Stopping.")
                    return

            # Wait for 0.3 second before capturing the next screen
            time.sleep(0.3)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")


if __name__ == "__main__":
    main()