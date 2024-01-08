easter_bread_count = int(input())
best_score = 0
best_baker = ""
for _ in range(easter_bread_count):
    baker_name = input()
    command = input()
    sum_of_score = 0
    while command != "Stop":
        current_score = int(command)
        sum_of_score += current_score
        command = input()
    print(f"{baker_name} has {sum_of_score} points.")
    if sum_of_score > best_score:
        best_score = sum_of_score
        best_baker = baker_name
        print(f"{best_baker} is the new number 1!")
print(f"{best_baker} won competition with {best_score} points!")
