import math

series = input()
episode_length = int(input())
lunch_break_length = int(input())
lunch_time = lunch_break_length / 8
rest_time = lunch_break_length / 4

available_time_for_series = lunch_break_length - lunch_time - rest_time
time_left = abs(available_time_for_series - episode_length)

if episode_length <= available_time_for_series:
    print(f"You have enough time to watch {series} and left with {math.ceil(time_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {math.ceil(time_left)} more minutes.")
