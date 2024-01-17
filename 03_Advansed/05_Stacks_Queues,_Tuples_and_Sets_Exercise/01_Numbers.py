first_sequences = set(int(el) for el in input().split())
second_sequences = set(int(el) for el in input().split())
commands = {
    "Add First": lambda x: [first_sequences.add(int(el)) for el in x],
    "Add Second": lambda x: [second_sequences.add(int(el)) for el in x],
    "Remove First": lambda x: [first_sequences.discard(int(el)) for el in x],
    "Remove Second": lambda x: [second_sequences.discard(int(el)) for el in x],
    "Check Subset": lambda x: print(first_sequences.issubset(second_sequences)
                                    or second_sequences.issubset(first_sequences))
}
for _ in range(int(input())):
    command1, command2, *numbers = input().split()

    command = command1 + " " + command2

    commands[command](numbers)

print(*sorted(first_sequences), sep=", ")
print(*sorted(second_sequences), sep=", ")
