companions_count = int(input())
days = int(input())

coins = 0

for day in range(1, days + 1):

    if day % 10 == 0:
        companions_count -= 2  # two companions leave every tenth day

    if day % 15 == 0:
        companions_count += 5

    coins += 50                 # add and subtract coins is after joining or leaving a companion
    coins -= companions_count * 2

    if day % 3 == 0:  # if third day:
        coins -= companions_count * 3  # minus 3 gold per person in party for motivation

    if day % 5 == 0:
        coins += companions_count * 20  # if fifth day:
        if day % 5 == 0 and day % 3 == 0:  # and motivation in same day
            coins -= companions_count * 2  # minus 2 additional coins

coins_per_companion = int(coins / companions_count)  # round coins as it can't split
print(f"{companions_count} companions received {coins_per_companion} coins each.")
