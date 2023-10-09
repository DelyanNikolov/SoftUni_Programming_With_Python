def data_type(comm, some_string):
    if comm == "int":
        return int(some_string) * 2
    elif comm == "real":
        return f"{(float(some_string) * 1.5):.2f}"
    elif comm == "string":
        return f"${some_string}$"


command = input()
data = input()
print(data_type(command, data))
