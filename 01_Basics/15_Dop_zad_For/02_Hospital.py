# Вход
# Входът се чете от конзолата и съдържа:
# •	На първия ред – периода, за който трябва да направите изчисления. Цяло число в интервала [1 ... 1000]
# •	На следващите редове(равни на броят на дните) – броя пациенти, които пристигат за преглед за текущия ден. Цяло число в интервала [0…10 000]
period = int(input())
doctors_count = 7
treated_patients = 0
untreated_patients = 0
for current_day in range(1, period + 1):
    patients_count = int(input())
    if current_day % 3 == 0:
        if untreated_patients > treated_patients:
            doctors_count += 1
    if patients_count <= doctors_count:
        treated_patients += patients_count
    else:
        treated_patients += doctors_count
        untreated_patients += patients_count - doctors_count

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
