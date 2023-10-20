import os

def delete_missing_labels(image_folder, label_folder):
    deleted_labels_count = 0

    # Get a list of image file names without extensions
    image_files = {os.path.splitext(file)[0] for file in os.listdir(image_folder) if file.lower().endswith(('.jpg', '.jpeg', '.png'))}

    # Iterate through label files and delete if corresponding image is not found
    for root, _, files in os.walk(label_folder):
        for file_name in files:
            label_file_path = os.path.join(root, file_name)
            label_name, label_extension = os.path.splitext(file_name)

            # Check if corresponding image file exists
            if label_name not in image_files:
                os.remove(label_file_path)
                print(f"Deleted label: {label_file_path}")
                deleted_labels_count += 1

    print(f"Number of labels deleted: {deleted_labels_count}")

# Example usage
image_folder_path = '/home/dsal/sriram/surgical_instruments/training/heart_multi_dataset/heart_total/heart_images'
label_folder_path = '/home/dsal/sriram/surgical_instruments/training/heart_multi_dataset/heart_total/heart_labels'
delete_missing_labels(image_folder_path, label_folder_path)
