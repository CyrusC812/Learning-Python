import os
os.chdir("/Users/chung/OneDrive/Documents/CADmodels/XLTimingBeltPulley_4-24teeths")
print(os.getcwd())
for f in os.listdir():
    f_title, f_ext = os.path.splitext(f)
    print(f.title)