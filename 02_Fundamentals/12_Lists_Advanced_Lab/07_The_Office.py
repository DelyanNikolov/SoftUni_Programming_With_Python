
employee_happiness = list(map(int, input().split()))
happiness_factor = int(input())
improved_happiness = [employee * happiness_factor for employee in employee_happiness]
average_happiness = sum(improved_happiness) / len(improved_happiness)
happy_count = len([person for person in improved_happiness if person >= average_happiness])
total_count = len(improved_happiness)
if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
