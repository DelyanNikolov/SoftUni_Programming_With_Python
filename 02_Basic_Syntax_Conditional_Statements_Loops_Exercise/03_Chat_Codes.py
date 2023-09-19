# If the number is 88 - "Hello"
# If the number is 86 - "How are you?"
# If the number is not 88 nor 86, and it is below 88 - "GREAT!"
# If the number is over 88 - "Bye."
number_of_messages = int(input())

for _ in range(number_of_messages):
    code = int(input())
    if code == 88:
        print("Hello")
    elif code == 86:
        print("How are you?")
    elif (code != 88 or code != 86) and code < 88:
        print("GREAT!")
    elif code > 88:
        print("Bye.")
