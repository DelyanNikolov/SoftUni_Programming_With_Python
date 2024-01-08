

months = int(input())
electricity_cost = 0
other_costs = 0
for _ in range(months):
    electricity_bill_every_month = float(input())
    electricity_cost += electricity_bill_every_month
    other_costs += electricity_bill_every_month + 20 + 15 + (electricity_bill_every_month + 20 + 15) * 0.2

water_cost = 20 * months
internet_cost = 15 * months
average_costs = (electricity_cost + water_cost + internet_cost + other_costs) / months

print(f"Electricity: {electricity_cost:.2f} lv")
print(f"Water: {water_cost:.2f} lv")
print(f"Internet: {internet_cost:.2f} lv")
print(f"Other: {other_costs:.2f} lv")
print(f"Average: {average_costs:.2f} lv")

