import os
file_name = "numbers.txt"
path = os.path.join("exercise_files", file_name)
total_sum = 0
with open(path, "r") as numbers_file:
    for item in numbers_file.readlines():
        total_sum += int(item.strip())
print(total_sum)