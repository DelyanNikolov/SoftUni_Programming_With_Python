sequence_of_numbers = [int(num) for num in input().split(", ")]
group = 10
while sequence_of_numbers:
    filtered_numbers = [num for num in sequence_of_numbers if num <= group]
    print(f"Group of {group}'s: {filtered_numbers}")
    group += 10
    sequence_of_numbers = [num for num in sequence_of_numbers if num not in filtered_numbers]
