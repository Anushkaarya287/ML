import cv2
import os

folder_path = os.path.dirname(os.path.abspath(__file__))

for file_name in os.listdir(folder_path):
    if file_name.lower().endswith((".jpg", ".png", ".jpeg")):
        file_path = os.path.join(folder_path, file_name)

        img = cv2.imread(file_path)

        if img is None:
            print(f"Could not read {file_name}")
            continue

        print(f"Image: {file_name}")
        print(f"Shape (H, W, C): {img.shape}")

