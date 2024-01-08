locations_count = int(input())

for _ in range(locations_count):
    expected_yield_of_gold = float(input())
    days_digging = int(input())
    total_gold_dug = 0
    for current_day in range(days_digging):
        gold_dug_for_current_day = float(input())
        total_gold_dug += gold_dug_for_current_day
    average_gold_dug = total_gold_dug / days_digging
    diff = expected_yield_of_gold - average_gold_dug
    if average_gold_dug >= expected_yield_of_gold:
        print(f"Good job! Average gold per day: {average_gold_dug :.2f}.")
    else:
        print(f"You need {diff :.2f} gold.")
