TOMS_TIME_FOR_PLAY = 30000
AFTER_WORK_PLAY_TIME = 63
DAY_OFF_PLAY_TIME = 127

days_off_count = int(input())
days_after_work_play = 365 - days_off_count

total_play_time = days_off_count * DAY_OFF_PLAY_TIME + days_after_work_play * AFTER_WORK_PLAY_TIME
time_left = abs(TOMS_TIME_FOR_PLAY - total_play_time)

hours = time_left // 60
minutes = time_left % 60

if total_play_time > TOMS_TIME_FOR_PLAY:
    print(f"Tom will run away\n"
          f"{hours} hours and {minutes} minutes more for play")
else:
    print(f"Tom sleeps well\n"
          f"{hours} hours and {minutes} minutes less for play")
