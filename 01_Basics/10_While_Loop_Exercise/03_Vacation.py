#
# money_needed = float(input())
# owned_money = float(input())
# days_count = 0
# spending_days_count = 0
# failed = False
# while owned_money < money_needed:
#     action = input()
#     money = float(input())
#     if action == "save":
#         owned_money += money
#         days_count += 1
#         spending_days_count = 0
#         continue
#     elif action == "spend":
#         owned_money -= money
#         if owned_money < 0:
#             owned_money = 0
#         spending_days_count += 1
#         days_count += 1
#         if spending_days_count >= 5:
#             failed = True
#             break
# if failed == True:
#     print("You can't save the money.")
#     print(f"{days_count}")
# else:
#     print(f"You saved the money for {days_count} days.")

# Step 1 collect the user inputs
target_money = float(input())
current_money = float(input())
# initialize some variables with empty values
days_counter = 0
spending_counter = 0

# Step 2 start the while loop
while current_money < target_money and spending_counter < 5:
    action = input()
    amount = float(input())
    days_counter += 1

    if action == "save":
        current_money += amount
        spending_counter = 0
    elif action == "spend":
        current_money -= amount
        spending_counter += 1
        if current_money < 0:
            current_money = 0

if spending_counter == 5:
    print("You can't save the money.")
    print(days_counter)
else:
    print(f"You saved the money for {days_counter} days.")
