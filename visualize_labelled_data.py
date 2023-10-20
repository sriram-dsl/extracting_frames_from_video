import cv2
import os

# Paths to the images and labels folders
images_folder = '/home/dsal/sriram/surgical_instruments/training/colon_surgery/colon_surgery_2_cloth/Colon surgery All tools/image'
labels_folder = '/home/dsal/sriram/surgical_instruments/training/colon_surgery/colon_surgery_2_cloth/Colon surgery All tools/labels'

# List all image files
image_files = os.listdir(images_folder)

# Desired resized dimensions
resize_width, resize_height = 640, 640

# Set the frame rate (1 frame per second)
frame_rate = 1

# Iterate over all images and display them at the specified frame rate
for image_file in image_files:
    # Load the image
    image_path = os.path.join(images_folder, image_file)
    image = cv2.imread(image_path)

    # Resize the image to 640x640
    resized_image = cv2.resize(image, (resize_width, resize_height))

    # Load corresponding label file
    label_file = os.path.join(labels_folder, image_file.replace('.jpg', '.txt').replace('.png', '.txt'))
    
    # If label file does not exist, print the image name and skip to the next image
    if not os.path.exists(label_file):
        print(f"No label found for image: {image_file}")
        continue
    
    with open(label_file, 'r') as f:
        lines = f.readlines()

    # Draw bounding boxes on the image
    for line in lines:
        # Parse label information (format: class_id x_center y_center width height)
        class_id, x_center, y_center, width, height = map(float, line.strip().split())
        
        # Convert relative coordinates to absolute coordinates
        x_center, y_center, width, height = int(x_center * resize_width), int(y_center * resize_height), int(width * resize_width), int(height * resize_height)
        
        # Calculate bounding box coordinates
        x1, y1, x2, y2 = int(x_center - width/2), int(y_center - height/2), int(x_center + width/2), int(y_center + height/2)
        
        # Draw bounding box on the image
        color = (0, 255, 0)  # Green color for the bounding box
        thickness = 2
        resized_image = cv2.rectangle(resized_image, (x1, y1), (x2, y2), color, thickness)

    # Display the labeled image
    cv2.imshow('Labeled Image', resized_image)
    cv2.waitKey(1000 // frame_rate)  # Delay to achieve the desired frame rate (in milliseconds)

# Release OpenCV window
cv2.destroyAllWindows()
