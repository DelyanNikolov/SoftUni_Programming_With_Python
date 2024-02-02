import os
from string import punctuation

file_name = "text.txt"
path = os.path.join("exercise_files", file_name)

output_file_name = "output.txt"
output_path = os.path.join("exercise_files", output_file_name)

with open(path, "r") as text_file:
    content = [line.strip() for line in text_file.readlines()]

output_file = open(output_path, "w")
for line in range(len(content)):
    letters_count, punctuation_count = 0, 0

    for symbol in content[line]:
        if symbol.isalpha():
            letters_count += 1
        elif symbol in punctuation:
            punctuation_count += 1
    new_line = f"Line {line + 1}: {content[line]} ({letters_count})({punctuation_count})\n"
    output_file.write(new_line)
output_file.close()
