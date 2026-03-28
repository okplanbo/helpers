# pip install pillow imagehash tqdm

# Optional (for HEIC support on macOS):
# pip install pillow-heif

import os
from PIL import Image
import imagehash
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm

folder_a = "/path/to/folderA"
folder_b = "/path/to/folderB"
threshold = 6
workers = os.cpu_count()

extensions = (".jpg",".jpeg",".png",".heic",".tiff",".bmp",".webp")

def get_images(folder):
    paths = []
    for root, _, files in os.walk(folder):
        for f in files:
            if f.lower().endswith(extensions):
                paths.append(os.path.join(root,f))
    return paths

def hash_image(path):
    try:
        img = Image.open(path)
        h = imagehash.phash(img)
        return (path, h)
    except:
        return None


# -------- BK TREE --------

class BKTree:
    def __init__(self, distfn):
        self.distfn = distfn
        self.tree = None

    def add(self, item):
        node = self.tree
        if node is None:
            self.tree = (item, {})
            return

        while True:
            parent, children = node
            d = self.distfn(item, parent)

            if d in children:
                node = children[d]
            else:
                children[d] = (item, {})
                break

    def search(self, item, threshold):
        if self.tree is None:
            return []

        candidates = [self.tree]
        results = []

        while candidates:
            parent, children = candidates.pop()
            d = self.distfn(item, parent)

            if d <= threshold:
                results.append(parent)

            low = d - threshold
            high = d + threshold

            for dist in children:
                if low <= dist <= high:
                    candidates.append(children[dist])

        return results


def hash_distance(a,b):
    return a[1] - b[1]


# -------- HASH FOLDER A --------

paths_a = get_images(folder_a)

print("Hashing folder A...")
with ProcessPoolExecutor(max_workers=workers) as ex:
    hashes_a = list(filter(None, tqdm(ex.map(hash_image, paths_a), total=len(paths_a))))

# build BK-tree
tree = BKTree(hash_distance)

for item in hashes_a:
    tree.add(item)

# -------- HASH + SEARCH FOLDER B --------

paths_b = get_images(folder_b)

matches = []

print("Searching matches...")
with ProcessPoolExecutor(max_workers=workers) as ex:
    for result in tqdm(ex.map(hash_image, paths_b), total=len(paths_b)):
        if not result:
            continue

        found = tree.search(result, threshold)

        for match in found:
            matches.append((match[0], result[0]))

# -------- SAVE RESULTS --------

with open("matches.txt","w") as f:
    for i,(a,b) in enumerate(matches,1):
        f.write(f"match{i}:\n{a}\n{b}\n\n")

print(f"Done. {len(matches)} matches saved.")

# Optional improvement:
# Switch from perceptual hash to deep image embeddings using OpenCLIP or models inspired by OpenAI’s CLIP.
# Benefits:
# finds same scene even if heavily cropped
# detects memes, edits, color changes
# works more like Google Photos duplicate detection

# Requires:
# PyTorch
# ~1–2 GB model
# slightly slower hashing