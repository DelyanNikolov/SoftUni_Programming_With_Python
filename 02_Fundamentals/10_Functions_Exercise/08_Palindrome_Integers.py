def is_palindrome(num):
    if num == num[::-1]:
        return True
    return False


list_of_numbers = input().split(", ")
for number in list_of_numbers:
    print(is_palindrome(number))
