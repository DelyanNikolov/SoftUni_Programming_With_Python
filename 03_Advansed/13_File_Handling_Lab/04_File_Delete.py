import os
file_name = "my_first_file.txt"
text_content = "I just created my first file!"

path = os.path.join("exercise_files", file_name)

try:
    os.remove(path)
except FileNotFoundError:
    print("File already deleted!")
