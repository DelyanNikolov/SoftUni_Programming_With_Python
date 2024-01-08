# Да се напише програма, която чете час и минути от 24-часово денонощие,
# въведени от потребителя и изчислява колко ще е часът след 15 минути.
# Резултатът да се отпечата във формат часове:минути. Часовете винаги са между 0 и 23,
# а минутите винаги са между 0 и 59. Часовете се изписват с една или две цифри.
# Минутите се изписват винаги с по две цифри, с водеща нула, когато е необходимо.

hours = int(input())
minutes = int(input())

time_in_minutes = hours * 60 + minutes + 15

hours_plus_15_minutes = time_in_minutes // 60
minutes_plus_15_minutes = time_in_minutes % 60

if hours_plus_15_minutes >= 24:
    hours_plus_15_minutes = 0
    if minutes_plus_15_minutes < 10:
        print(f"{hours_plus_15_minutes}:0{minutes_plus_15_minutes}")
    else:  print(f"{hours_plus_15_minutes}:{minutes_plus_15_minutes}")
elif minutes_plus_15_minutes < 10:
    print(f"{hours_plus_15_minutes}:0{minutes_plus_15_minutes}")
else:  print(f"{hours_plus_15_minutes}:{minutes_plus_15_minutes}")


