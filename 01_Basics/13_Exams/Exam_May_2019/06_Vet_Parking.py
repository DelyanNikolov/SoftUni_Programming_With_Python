days_count = int(input())
hours_count = int(input())
total_stay_tax = 0
for current_day in range(1, days_count + 1):
    total_tax = 0
    for current_hour in range(1, hours_count + 1):
        if current_day % 2 == 0 and current_hour % 2 != 0:
            daily_tax = 2.50
        elif current_day % 2 != 0 and current_hour % 2 == 0:
            daily_tax = 1.25
        else:
            daily_tax = 1
        total_tax += daily_tax
        total_stay_tax += daily_tax
    print(f"Day: {current_day} - {total_tax :.2f} leva")
print(f"Total: {total_stay_tax :.2f} leva")
