from math import ceil
first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
students_count = int(input())

total_service_time = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency

time_needed = 0
while True:
    if students_count > 0:
        students_count -= total_service_time
        time_needed += 1
        if time_needed % 4 == 0:
            time_needed += 1
    else:
        break
print(f"Time needed: {ceil(time_needed)}h.")
