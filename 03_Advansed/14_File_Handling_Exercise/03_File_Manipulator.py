import os

while True:
    command, *attributes = input().split("-")

    if command == "End":
        break

    elif command == "Create":
        file_name = attributes[0]
        path = os.path.join("exercise_files", file_name)
        with open(path, "w") as file:
            pass

    elif command == "Add":
        file_name = attributes[0]
        content = attributes[1]
        path = os.path.join("exercise_files", file_name)
        with open(path, "a") as file:
            file.write(content)

    elif command == "Replace":
        file_name = attributes[0]
        old_string = attributes[1]
        new_string = attributes[2]
        path = os.path.join("exercise_files", file_name)
        try:
            with open(path, "r+") as file:
                content = file.read()
                content = content.replace(old_string, new_string)
                file.seek(0)  # returns cursor at beginning
                file.truncate()  # clips old file to fit new content
        except FileNotFoundError:
            print(f"An error occurred!")
    elif command == "Delete":
        file_name = attributes[0]
        path = os.path.join("exercise_files", file_name)
        try:
            os.remove(path)
        except FileNotFoundError:
            print(f"An error occurred!")
