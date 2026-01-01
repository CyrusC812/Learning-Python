# 14 - Automating renaming files

### Overview
How to automate file renaming, I used one of my folders that contained messy CAD .step files as example
## Key Concepts
### Striping and cleaning files
- use os.path.splitext(f) to split extension from a file
- use f.strip() to remove empty white spaces
- use zfill(2) to pad numbers , like from 2 to 02
### Other useful commands when automating file renaming
- os.rename(f,new_name) to actually rename it
- use fstrings to construct a new name for file
### Important Details
> Automating renaming files are very useful when folders are large and messy , they save a lot of time
### Examples
- Using os module, and a for file loop to rename my .step files to "XLTimmingBeltPulley_{teeth}Teeths{ext}"
  ```python
    import os,re
    os.chdir("/Users/chung/OneDrive/Documents/CADmodels/XLTimingBeltPulley_4-24teeths")
    print(os.getcwd())
    FOLDER = os.getcwd()
    for f in os.listdir(FOLDER):
        old_path = os.path.join(FOLDER, f)
        print("old_path : ",old_path)
        if not os.path.isfile(old_path):
            continue

        name, ext = os.path.splitext(f)

        match = re.search(r"\d+", name)
        if not match:
            print(f"Skipping (no number): {f}")
            continue

        teeth = match.group().zfill(2)

        new_name = f"XLTimingBeltPulley_{teeth}Teeths{ext}"
        new_path = os.path.join(FOLDER, new_name)

        print(f"{f}  ->  {new_name}")
        os.rename(old_path, new_path)

        