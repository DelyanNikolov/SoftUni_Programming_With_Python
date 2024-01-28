from collections import deque

peaks_data = deque([("Vihren", 80), ("Kutelo", 90), ("Banski Suhodol", 100), ("Polezhan", 60), ("Kamenitza", 70)])

conquered_peaks = []
food_portions = [int(x) for x in input().split(", ")]
stamina_supply = deque([int(s) for s in input().split(", ")])

for day in range(7):
    daily_food = food_portions.pop()
    daily_stamina = stamina_supply.popleft()
    climber_points = daily_food + daily_stamina

    if peaks_data:
        current_peak = peaks_data.popleft()
        current_peak_points = current_peak[1]
        current_peak_name = current_peak[0]
    else:
        break
    if climber_points >= current_peak_points:
        conquered_peaks.append(current_peak_name)
    else:
        peaks_data.appendleft(current_peak)

if peaks_data:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
else:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")

if conquered_peaks:
    print("Conquered peaks:")
    [print(peak) for peak in conquered_peaks]
