destination = input()

while destination != "End":
    budget = float(input())
    sum_of_money = 0
    while sum_of_money < budget:
        current_money = float(input())
        sum_of_money += current_money
    print(f"Going to {destination}!")
    destination = input()
