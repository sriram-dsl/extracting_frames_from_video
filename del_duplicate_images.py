import os
import hashlib

def get_file_hash(file_path):
    """Generate a hash for a given file."""
    hasher = hashlib.sha1()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(65536)  # 64k chunks
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

def find_and_delete_duplicates(source_folder, target_folder):
    source_image_hashes = set()
    deleted_images_count = 0

    # Generate hashes for images in the source folder
    for root, _, files in os.walk(source_folder):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
                file_hash = get_file_hash(file_path)
                source_image_hashes.add(file_hash)

    # Iterate through images in the target folder and delete duplicates
    for root, _, files in os.walk(target_folder):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
                file_hash = get_file_hash(file_path)
                if file_hash in source_image_hashes:
                    os.remove(file_path)
                    print(f"Deleted duplicate image: {file_path}")
                    deleted_images_count += 1

    print(f"Number of images deleted: {deleted_images_count}")

# Example usage
source_folder_path = '/home/dsal/sriram/surgical_instruments/training/heart_multi_dataset/heart_1/heart_images_2' # unique images path
target_folder_path = '/home/dsal/sriram/surgical_instruments/training/heart_multi_dataset/heart_total/heart_images # all images path'
find_and_delete_duplicates(source_folder_path, target_folder_path)
