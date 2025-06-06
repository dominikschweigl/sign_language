import os
import shutil
import pandas as pd
from PIL import Image

# CONFIGURATION
image_folder = "images"           # Folder containing original images
label_csv = "labels.csv"         # CSV file without header
output_csv = "labels_all2.csv"
# target_labels = ["1", "2", "3", "5", "7", "a", "e", "f", "h", "m", "n", "o", "q", "r", "t", "w", "x"]                # Label you want to filter
target_labels = ["8", "b", "d", "i", "j", "k", "s", "v", "y"] 
output_folder = "manipulated_images" # Where to save matching images
apply_transformation = True       # Set to False to just copy

# Make sure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Load label CSV (no header)
labels_df = pd.read_csv(label_csv, header=None)
labels_df.columns = ["label", "imagepath"]

augmented_df = labels_df.copy().iloc[0:0]

# Loop through and process images with the target label
for idx, row in labels_df.iterrows():
    label = row['label']
    if str(label) in target_labels:
        filename = str(row["imagepath"]).split(".")[0]
        src_path = os.path.join(image_folder, filename + ".jpg")

        if os.path.exists(src_path):
            img = Image.open(src_path)

            if apply_transformation:
                img2 = img.transpose(Image.FLIP_LEFT_RIGHT) 
                dst_path = os.path.join(output_folder, filename + "_flipped_lr.jpg")
                img2.save(dst_path)
                augmented_df.loc[len(augmented_df)] = [label, filename + "_flipped_lr.jpg"]
                
                # img2 = img.transpose(Image.FLIP_TOP_BOTTOM) 
                # dst_path = os.path.join(output_folder, filename + "_flipped_tb.jpg")
                # img2.save(dst_path)
                # augmented_df.loc[len(augmented_df)] = [label, filename + "_flipped_tb.jpg"]
                
                img2 = img.rotate(90)
                dst_path = os.path.join(output_folder, filename + "_rotated_90.jpg")
                img2.save(dst_path)
                augmented_df.loc[len(augmented_df)] = [label, filename + "_rotated_90.jpg"]
                
                # img2 = img.rotate(180)
                # dst_path = os.path.join(output_folder,  filename + "_rotated_180.jpg")
                # img2.save(dst_path)
                # augmented_df.loc[len(augmented_df)] = [label, filename + "_rotate_180.jpg"]
                
                # img2 = img.rotate(270)
                # dst_path = os.path.join(output_folder, filename +"_rotated_270.jpg")
                # img2.save(dst_path)
                # augmented_df.loc[len(augmented_df)] = [label, filename + "_rotate_270.jpg"]

        else:
            print(f"Image not found: {src_path}")

augmented_df.to_csv(output_csv, header=False, index=False)