import os

files = [f for f in os.listdir(
    "./") if os.path.isfile(f) and f.split(".")[1] == "html"]

files.sort()
for file in files:
    print(f"<a href='{file}'>{file}</a>")
