
exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

minutes_exam = exam_hour * 60 + exam_minutes
minutes_arrival = arrival_hour * 60 + arrival_minutes

if minutes_exam < minutes_arrival:
    print("Late")
    if 60 > minutes_arrival - minutes_exam > 0:
        mm = minutes_arrival - minutes_exam
        print(f"{mm} minutes after the start")
    elif minutes_arrival - minutes_exam >= 60:
        mm = (minutes_arrival - minutes_exam) % 60
        hh = (minutes_arrival - minutes_exam) // 60
        if mm < 10:
            print(f"{hh}:0{mm} hours after the start")
        else:
            print(f"{hh}:{mm} hours after the start")
elif (minutes_exam - 30) <= minutes_arrival <= minutes_exam:
    print("On time")
elif minutes_exam - 30 > minutes_arrival:
    print("Early")

if 60 > minutes_exam - minutes_arrival > 0:
    mm = minutes_exam - minutes_arrival
    if mm < 10:
        print(f"{mm} minutes before the start")
    else:
        print(f"{mm} minutes before the start")
elif minutes_exam - minutes_arrival >= 60:
    mm = (minutes_exam - minutes_arrival) % 60
    hh = (minutes_exam - minutes_arrival) // 60
    if mm < 10:
        print(f"{hh}:0{mm} hours before the start")
    else:
        print(f"{hh}:{mm} hours before the start")
