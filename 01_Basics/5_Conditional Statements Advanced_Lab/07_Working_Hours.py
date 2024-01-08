work_hour = int(input())
day_of_week = input()

state = "closed"

if day_of_week == "Monday":
    if 10 <= work_hour <= 18:
        state = "open"
elif day_of_week == "Tuesday":
    if 10 <= work_hour <= 18:
        state = "open"
elif day_of_week == "Wednesday":
    if 10 <= work_hour <= 18:
        state = "open"
elif day_of_week == "Thursday":
    if 10 <= work_hour <= 18:
        state = "open"
elif day_of_week == "Friday":
    if 10 <= work_hour <= 18:
        state = "open"
elif day_of_week == "Saturday":
    if 10 <= work_hour <= 18:
        state = "open"

print(state)
