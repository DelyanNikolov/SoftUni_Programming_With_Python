command = input()
total_tickets_sold = 0
total_student_tickets = 0
total_standard_tickets = 0
total_kids_tickets = 0
while command != "Finish":
    name_of_movie = command
    sum_of_movie_tickets = 0
    student_tickets_count = 0
    standard_tickets_count = 0
    kids_tickets_count = 0
    available_seats = int(input())
    for _ in range(available_seats):
        ticket_type = input()  # "student", "standard", "kid"е
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets_count += 1
        elif ticket_type == "standard":
            standard_tickets_count += 1
        elif ticket_type == "kid":
            kids_tickets_count += 1
    sum_of_movie_tickets += (student_tickets_count + standard_tickets_count + kids_tickets_count)
    percent_of_hall_seats = sum_of_movie_tickets / available_seats * 100
    print(f"{name_of_movie} - {percent_of_hall_seats :.2f}% full.")
    total_tickets_sold += sum_of_movie_tickets
    total_student_tickets += student_tickets_count
    total_standard_tickets += standard_tickets_count
    total_kids_tickets += kids_tickets_count
    command = input()
# •	При получаване на командата "Finish" да се отпечатат четири реда:
students_percentage = total_student_tickets / total_tickets_sold * 100
standard_percentage = total_standard_tickets / total_tickets_sold * 100
kids_percentage = total_kids_tickets / total_tickets_sold * 100
print(f"Total tickets: {total_tickets_sold}")
print(f"{students_percentage :.2f}% student tickets.")
print(f"{standard_percentage :.2f}% standard tickets.")
print(f"{kids_percentage :.2f}% kids tickets.")
