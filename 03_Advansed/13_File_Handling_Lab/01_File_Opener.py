import os
file_name = "text.txt"
path = os.path.join("exercise_files", file_name)
try:
    with open(path, "r") as text_file:
        print("File found")
except FileNotFoundError:
    print("File not found")
