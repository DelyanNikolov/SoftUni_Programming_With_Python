judges_count = int(input())
score_of_all_presentations = 0
presentations_count = 0

command = input()
while not command == "Finish":
    presentation_name = command
    sum_of_scores = 0
    for _ in range(judges_count):
        current_score = float(input())
        sum_of_scores += current_score
        score_of_all_presentations += current_score
    average_score = sum_of_scores / judges_count
    print(f"{presentation_name} - {average_score :.2f}.")
    presentations_count += 1

    command = input()
    average_score_of_all_presentations = score_of_all_presentations / (presentations_count * judges_count)
print(f"Student's final assessment is {average_score_of_all_presentations :.2f}.")
