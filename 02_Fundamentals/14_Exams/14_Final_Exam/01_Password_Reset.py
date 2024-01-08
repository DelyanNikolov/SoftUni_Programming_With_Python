the_string = input()
command = input().split()
row_password = the_string  # Initialize row_password with the original string

while not command[0] == "Done":
    if command[0] == "TakeOdd":
        row_password = row_password[1::2]  # Take odd-indexed characters
        print(row_password)
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        substring = row_password[index:index+length]
        row_password = row_password.replace(substring, "", 1)
        print(row_password)
    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in row_password:
            row_password = row_password.replace(substring, substitute)
            print(row_password)
        else:
            print("Nothing to replace!")
    command = input().split()

print(f"Your password is: {row_password}")
