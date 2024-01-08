def check_length(username):
    """checks is the username length is correct
    between 3 and 16 chars."""
    if 3 <= len(username) <= 16:
        return True
    return False


def check_characters_valid(username):
    for char in username:
        if not (char.isalnum() or char == "-" or char == "_"):
            return False
    return True


def check_redundant_symbols(username):
    for char in username:
        if char == " ":
            return False
    return True


def is_username_valid(username):
    if check_length(username) and check_characters_valid(username) and check_redundant_symbols(username):
        return True
    return False


usernames_list = input().split(", ")
for some_username in usernames_list:
    if is_username_valid(some_username):
        print(some_username)
