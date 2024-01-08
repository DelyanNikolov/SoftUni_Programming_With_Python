actor_name = input()
points_from_academy = float(input())
jury_count = int(input())
sum_of_points = points_from_academy
for _ in range(jury_count):
    name_of_jury = input()
    points_from_jury = float(input())
    sum_of_points += len(name_of_jury) * points_from_jury / 2
    if sum_of_points > 1250.5:
        break

if sum_of_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {sum_of_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {1250.5 - sum_of_points:.1f} more!")
