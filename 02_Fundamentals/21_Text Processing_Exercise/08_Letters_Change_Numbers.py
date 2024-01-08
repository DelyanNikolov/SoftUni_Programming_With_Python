def find_position_of_letter(letter: str):
    """finds the position of the letter in the alphabet"""
    if letter.isupper():
        return ord(letter) - 64
    return ord(letter) - 96


def calculate_points(problem):
    """calculates points to add to the total sum"""
    result_to_add = 0
    letter_in_front = problem[0]
    letter_in_back = problem[-1]
    number = int(problem[1:len(problem) - 1])
    if letter_in_front.isupper():
        position_of_letter = find_position_of_letter(letter_in_front)
        result_to_add += number / position_of_letter
    elif letter_in_front.lower():
        position_of_letter = find_position_of_letter(letter_in_front)
        result_to_add += number * position_of_letter
    if letter_in_back.isupper():
        position_of_letter = find_position_of_letter(letter_in_back)
        result_to_add -= position_of_letter
    elif letter_in_back.lower():
        position_of_letter = find_position_of_letter(letter_in_back)
        result_to_add += position_of_letter
    return result_to_add


# collecting information
list_of_strings = [item.strip() for item in input().split()]

result = 0
for item in list_of_strings:
    # calculating the sum of the current string and adding to result
    result += calculate_points(item)
print(f"{result:.2f}")
