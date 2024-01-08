def validate_password(some_password):
    errors = []
    if len(password) < 6 or len(password) > 10:
        errors.append("Password must be between 6 and 10 characters")
    if not password.isalnum():
        errors.append("Password must consist only of letters and digits")
    digits_counter = 0
    for character in some_password:
        if character.isdigit():
            digits_counter +=1
    if digits_counter < 2:
        errors.append("Password must have at least 2 digits")
    return errors


password = input()
errors_in_password = validate_password(password)
if not errors_in_password:
    print("Password is valid")
else:
    print("\n".join(validate_password(password)))
