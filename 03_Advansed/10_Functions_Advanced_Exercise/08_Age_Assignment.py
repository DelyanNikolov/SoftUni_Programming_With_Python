def age_assignment(*names, **ages):
    result = []
    # "{name} is {age} years old."
    for letter, age in ages.items():
        for name in names:
            if name.startswith(letter):
                result.append(f"{name} is {age} years old.")

    return '\n'.join(sorted(result))


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
