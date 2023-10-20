import os
from collections import defaultdict

def check_image_formats(folder_path):
    image_formats = defaultdict(int)

    # Iterate through files in the folder and count image formats
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            # Get the file extension and count the image format
            _, file_extension = os.path.splitext(file_name)
            image_formats[file_extension.lower()] += 1

    # Print the image formats and their counts
    print("Image Formats and Counts:")
    for format, count in image_formats.items():
        print(f"{format}: {count}")

    total_images = sum(image_formats.values())
    print(f"Total number of images: {total_images}")

# Example usage
folder_path = '/home/dsal/sriram/surgical_instruments/training/17_10/val/images'
check_image_formats(folder_path)
