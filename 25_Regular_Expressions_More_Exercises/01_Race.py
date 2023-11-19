import re

race_results = {}
list_of_racers = input().split(", ")
letters_pattern = r"[A-Za-z]"
numbers_pattern = r"\d"
while True:
    line = input()
    if line == "end of race":
        break
    letters = re.findall(letters_pattern, line)
    numbers = re.findall(numbers_pattern, line)
    racer_name = "".join(letters)
    distance_ran = sum([int(distance) for distance in numbers])

    if racer_name in list_of_racers and racer_name not in race_results.keys():
        race_results[racer_name] = 0
    if racer_name in race_results:
        race_results[racer_name] += distance_ran

sorted_score = sorted(race_results.items(), key=lambda x: -x[1])
print(f"1st place: {sorted_score[0][0]}")
print(f"2nd place: {sorted_score[1][0]}")
print(f"3rd place: {sorted_score[2][0]}")
