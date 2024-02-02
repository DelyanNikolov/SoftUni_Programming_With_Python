import os

symbols = ("-", ",", ".", "!", "?")

file_name = "text.txt"
path = os.path.join("exercise_files", file_name)

with open(path, "r") as text_file:
    content = [line.strip() for line in text_file.readlines()]  # get rid of the \n (new line) at end of every sentence

for row in range(0, len(content), 2):  # range is with step 2 to filter only even lines
    for symbol in symbols:
        content[row] = content[row].replace(symbol, "@")

    print(content[row][::-1])
