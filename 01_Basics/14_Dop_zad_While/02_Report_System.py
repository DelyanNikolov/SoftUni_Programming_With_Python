charity_money = int(input())
cash_or_card_counter = 1
cash_transactions = 0
card_transactions = 0
money_collected = 0
cash_transactions_count = 0
card_transactions_count = 0
while True:

    command = input()

    if command == "End":
        break

    current_money = int(command)
    cash_or_card_counter += 1
    if cash_or_card_counter % 2 == 0:
        if current_money > 100:
            print("Error in transaction!")

        else:
            cash_transactions += current_money
            cash_transactions_count += 1
            print("Product sold!")

    if cash_or_card_counter % 2 != 0:
        if current_money < 10:
            print("Error in transaction!")

        else:
            card_transactions += current_money
            card_transactions_count += 1
            print("Product sold!")
    money_collected = (cash_transactions + card_transactions)
    if money_collected >= charity_money:
        break
if command == "End":
    money_collected = (cash_transactions + card_transactions)
    if money_collected < charity_money:
        print("Failed to collect required money for charity.")
else:
    average_cash = cash_transactions / cash_transactions_count
    average_card = card_transactions / cash_transactions_count
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_card:.2f}")

