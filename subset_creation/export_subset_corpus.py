import shutil
import os

with open('subset_mls_list_FROZEN_05-08-2026.txt') as f:
    subset = [line.strip() for line in f]

source_dir = '/mnt/HDD3T/YenData/Calgary/Corpus'
dest_dir = 'subset_corpus'

os.makedirs(dest_dir, exist_ok=True)

copied = 0
missing = []
for mls in subset:
    filename = f"{mls}_corpus.txt"
    src = os.path.join(source_dir, filename)
    dst = os.path.join(dest_dir, filename)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        copied += 1
    else:
        missing.append(mls)

print(f"Copied {copied} corpus files")
if missing:
    print(f"Missing {len(missing)} files:", missing[:10], "..." if len(missing) > 10 else "")

# Also copy description.json files for later failure analysis
desc_copied = 0
for mls in subset:
    filename = f"{mls}_description.json"
    src = os.path.join(source_dir, filename)
    dst = os.path.join(dest_dir, filename)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        desc_copied += 1
print(f"Copied {desc_copied} description.json files")
