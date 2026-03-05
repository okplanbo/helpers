# Compares images from folder1 against images from folder2 and gives
# a list of matching ones. File sizes, compression and names may differ.

# pip3 install pillow imagehash tqdm
# python3 compare-images.py path1 path2

import os
import argparse
from PIL import Image
import imagehash
from tqdm import tqdm

# -------- CLI arguments --------

parser = argparse.ArgumentParser(description="Compare images between two folders using perceptual hashing.")
parser.add_argument("folder_a", help="Reference folder")
parser.add_argument("folder_b", help="Folder to compare against")
parser.add_argument("--threshold", type=int, default=5, help="Hash difference threshold (default: 5)")
parser.add_argument("--output", default="matches.txt", help="Output file (default: matches.txt)")

args = parser.parse_args()

folder_a = args.folder_a
folder_b = args.folder_b
threshold = args.threshold
output_file = args.output


hashes_a = {}
matches = []

# -------- COLLECT FILES --------

files_a = []
for root, _, files in os.walk(folder_a):
    for f in files:
        files_a.append(os.path.join(root, f))

files_b = []
for root, _, files in os.walk(folder_b):
    for f in files:
        files_b.append(os.path.join(root, f))


# -------- HASH FOLDER A --------

for path in tqdm(files_a, desc="Hashing folder A"):
    try:
        img = Image.open(path)
        h = imagehash.phash(img)
        hashes_a[path] = h
    except:
        pass


# -------- COMPARE WITH FOLDER B --------

for path_b in tqdm(files_b, desc="Comparing folder B"):
    try:
        img = Image.open(path_b)
        h_b = imagehash.phash(img)

        for path_a, h_a in hashes_a.items():
            if h_a - h_b <= threshold:
                matches.append((path_a, path_b))

    except:
        pass


# -------- SAVE RESULTS --------

with open(output_file, "w") as f:
    for i, (a, b) in enumerate(matches, 1):
        f.write(f"match{i}:\n{a}\n{b}\n\n")

print(f"{len(matches)} matches written to {output_file}")
