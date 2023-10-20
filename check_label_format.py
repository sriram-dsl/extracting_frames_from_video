import os
from collections import defaultdict

def check_label_formats(folder_path):
    label_formats = defaultdict(int)
    other_files_count = 0

    # Iterate through files in the folder and count label formats
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if file_name.lower().endswith(('.txt', '.xml')):
            # Get the file extension and count the label format
            _, file_extension = os.path.splitext(file_name)
            label_formats[file_extension.lower()] += 1
        else:
            other_files_count += 1

    # Print the label formats and their counts
    print("Label Formats and Counts:")
    for format, count in label_formats.items():
        print(f"{format}: {count}")

    total_labels = sum(label_formats.values())
    print(f"Total number of labels: {total_labels}")
    print(f"Number of files with other formats: {other_files_count}")

# Example usage
folder_path = '/home/dsal/sriram/surgical_instruments/training/17_10/val/labels'
check_label_formats(folder_path)
