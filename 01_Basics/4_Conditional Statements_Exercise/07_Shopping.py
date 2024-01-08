budget = float(input())
videocard_count = int(input())
processor_count = int(input())
ram_count = int(input())

VIDEOCARD_PRICE = 250
PROCESSOR_PRICE = 0.35 * videocard_count * VIDEOCARD_PRICE
RAM_PRICE = 0.10 * videocard_count * VIDEOCARD_PRICE
discount = 0

if videocard_count > processor_count:
    discount = 0.15

total_cost = (videocard_count * VIDEOCARD_PRICE
              + processor_count * PROCESSOR_PRICE
              + ram_count * RAM_PRICE) \
             * (1 - discount)

budget_left = budget - total_cost
budget_needed = total_cost - budget

if total_cost <= budget:
    print(f"You have {budget_left:.2f} leva left!")
else:
    print(f"Not enough money! You need {budget_needed:.2f} leva more!")
