import os,re
os.chdir("/Users/chung/OneDrive/Documents/CADmodels/XLTimingBeltPulley_4-24teeths")
print(os.getcwd())
FOLDER = os.getcwd()
for f in os.listdir(FOLDER):
    old_path = os.path.join(FOLDER, f)

    # skip folders
    if not os.path.isfile(old_path):
        continue

    name, ext = os.path.splitext(f)

    # extract the first number found (teeth count)
    match = re.search(r"\d+", name)
    if not match:
        print(f"Skipping (no number): {f}")
        continue

    teeth = match.group().zfill(2)

    new_name = f"XLTimingBeltPulley_{teeth}Teeths{ext}"
    new_path = os.path.join(FOLDER, new_name)

    print(f"{f}  ->  {new_name}")
    os.rename(old_path, new_path)

    