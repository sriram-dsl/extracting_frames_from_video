import os
import random
import shutil

# Set the source directories for images and labels
img_source_dir = '/home/dsal/sriram/surgical_instruments/training/augumentation_folder/heart_surgery/cloth/2023-10-20_12:41:03/images'  # Directory containing image files
lab_source_dir = '/home/dsal/sriram/surgical_instruments/training/augumentation_folder/heart_surgery/cloth/2023-10-20_12:41:03/labels'  # Directory containing label files

# Set the destination directories for training and validation sets
train_img_dest_dir = '/home/dsal/sriram/surgical_instruments/training/augumentation_folder/heart_surgery/cloth/2023-10-20_12:41:03/train_img'  # Destination directory for training images
train_lab_dest_dir = '/home/dsal/sriram/surgical_instruments/training/augumentation_folder/heart_surgery/cloth/2023-10-20_12:41:03/train_lab'  # Destination directory for training labels
val_img_dest_dir = '/home/dsal/sriram/surgical_instruments/training/augumentation_folder/heart_surgery/cloth/2023-10-20_12:41:03/val_img'      # Destination directory for validation images
val_lab_dest_dir = '/home/dsal/sriram/surgical_instruments/training/augumentation_folder/heart_surgery/cloth/2023-10-20_12:41:03/val_lab'      # Destination directory for validation labels

# Create destination directories if they don't exist
os.makedirs(train_img_dest_dir, exist_ok=True)
os.makedirs(train_lab_dest_dir, exist_ok=True)
os.makedirs(val_img_dest_dir, exist_ok=True)
os.makedirs(val_lab_dest_dir, exist_ok=True)

# List all image files in the source directory
img_files = [f for f in os.listdir(img_source_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

# Randomly shuffle the image files
random.shuffle(img_files)

# Calculate the number of images for training and validation
total_images = len(img_files)
train_ratio = 0.7
num_train = int(total_images * train_ratio)

# Split the images and labels into training and validation sets
train_img_files = img_files[:num_train]
val_img_files = img_files[num_train:]

# Move the image files to the corresponding training and validation directories
for img_file in train_img_files:
    shutil.move(os.path.join(img_source_dir, img_file), os.path.join(train_img_dest_dir, img_file))
for img_file in val_img_files:
    shutil.move(os.path.join(img_source_dir, img_file), os.path.join(val_img_dest_dir, img_file))

# Move the corresponding label files to the corresponding directories
for img_file in train_img_files:
    base_name, _ = os.path.splitext(img_file)
    lab_file_txt = base_name + ".txt"  # Assuming label files have the same name as the images
    lab_file_xml = base_name + ".xml"  # Assuming label files have the same name as the images
    if os.path.exists(os.path.join(lab_source_dir, lab_file_txt)):
        shutil.move(os.path.join(lab_source_dir, lab_file_txt), os.path.join(train_lab_dest_dir, lab_file_txt))
    elif os.path.exists(os.path.join(lab_source_dir, lab_file_xml)):
        shutil.move(os.path.join(lab_source_dir, lab_file_xml), os.path.join(train_lab_dest_dir, lab_file_xml))

for img_file in val_img_files:
    base_name, _ = os.path.splitext(img_file)
    lab_file_txt = base_name + ".txt"  # Assuming label files have the same name as the images
    lab_file_xml = base_name + ".xml"  # Assuming label files have the same name as the images
    if os.path.exists(os.path.join(lab_source_dir, lab_file_txt)):
        shutil.move(os.path.join(lab_source_dir, lab_file_txt), os.path.join(val_lab_dest_dir, lab_file_txt))
    elif os.path.exists(os.path.join(lab_source_dir, lab_file_xml)):
        shutil.move(os.path.join(lab_source_dir, lab_file_xml), os.path.join(val_lab_dest_dir, lab_file_xml))

print(f"Split {total_images} images into {len(train_img_files)} training and {len(val_img_files)} validation images.")
