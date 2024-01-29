numbers_dictionary = {}

line = input()
while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:  # catches Value error (if user inputs non integer value) and prints the corresponding message
        print("The variable number must be an integer")

    line = input()      # added input line to avoid infinite loop

line = input()
while line != "Remove":
    searched = line
    print(numbers_dictionary[searched])

    line = input()  # added input line to avoid infinite loop

line = input()
while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:    # catches Key error (if the user inputs non existing key) and prints the corresponding message
        print("Number does not exist in dictionary")

    line = input()  # added input line to avoid infinite loop

print(numbers_dictionary)
