path = input().split("\\")
file_name = ""
file_extension = ""
for item in path:
    if "." in item:
        file_data = item.split(".")
        file_name = file_data[0]
        file_extension = file_data[1]

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
# filepath = input().split("\\")
# filename_and_extension = filepath[-1]
# filename, extension = filename_and_extension.split(".")
# print(f"File name: {filename}")
# print(f"File extension: {extension}")
