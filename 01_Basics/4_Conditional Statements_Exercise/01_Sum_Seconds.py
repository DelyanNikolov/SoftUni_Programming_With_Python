import math

time_first = int(input())
time_second = int(input())
time_tird = int(input())

total_time = time_first + time_second + time_tird
minutes = math.floor(total_time // 60)
seconds = total_time % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else: print(f"{minutes}:{seconds}")