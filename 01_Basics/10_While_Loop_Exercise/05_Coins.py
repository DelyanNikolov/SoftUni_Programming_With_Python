change_amount = float(input())

coins_count = 0
change_amount_in_cents = int(change_amount * 100)
while change_amount_in_cents > 0:
    if change_amount_in_cents >= 200:
        change_amount_in_cents -= 200
    elif change_amount_in_cents >= 100:
        change_amount_in_cents -= 100
    elif change_amount_in_cents >= 50:
        change_amount_in_cents -= 50
    elif change_amount_in_cents >= 20:
        change_amount_in_cents -= 20
    elif change_amount_in_cents >= 10:
        change_amount_in_cents -= 10
    elif change_amount_in_cents >= 5:
        change_amount_in_cents -= 5
    elif change_amount_in_cents >= 2:
        change_amount_in_cents -= 2
    elif change_amount_in_cents >= 1:
        change_amount_in_cents -= 1

    coins_count += 1
print(coins_count)
