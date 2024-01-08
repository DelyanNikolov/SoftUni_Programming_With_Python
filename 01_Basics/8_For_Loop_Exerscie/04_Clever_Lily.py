
age = int(input())
price_of_washing_machine = float(input())
price_of_toys = int(input())

sum_of_money = 0
sum_of_toys = 0

for birthday in range(1, age +1):
    if birthday % 2 == 0:
        sum_of_money += birthday * 5 - 1
    else:
        sum_of_toys += price_of_toys

total_sum = sum_of_money + sum_of_toys
diff = abs(price_of_washing_machine - total_sum)

if price_of_washing_machine <= total_sum:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
