import csv
import os
from PIL import Image

INPUT_CSV = "crop_bounds.csv"
CROPPED_DIR = "cropped"

# Ensure output directory exists
os.makedirs(CROPPED_DIR, exist_ok=True)

with open(INPUT_CSV, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row["name"].strip()
        x_start = int(row["x_start"])
        y_start = int(row["y_start"])
        x_end = int(row["x_end"])
        y_end = int(row["y_end"])

        for suffix in ["before", "after"]:
            filename = f"{name}_{suffix}.jpg"
            if not os.path.exists(filename):
                print(f"File not found: {filename}")
                continue

            # Open image and crop
            with Image.open(filename) as img:
                cropped = img.crop((x_start, y_start, x_end, y_end))
                output_path = os.path.join(CROPPED_DIR, filename)
                cropped.save(output_path)
                print(f"Cropped and saved: {output_path}")