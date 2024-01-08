set_size = input()  # "small" или "big"
sets_ordered = int(input())
total_cost = 0
small_set_price = 0
large_set_price = 0
fruit = ""

if fruit == "Watermelon":
    small_set_price = 56
    large_set_price = 28.70
elif fruit == "Mango":
    small_set_price = 36.66
    large_set_price = 19.60
elif fruit == "Pineapple":
    small_set_price = 42.10
    large_set_price = 24.80
elif fruit == "Raspberry":
    small_set_price = 20
    large_set_price = 15.20
if set_size == "small":
    total_cost = 2 * sets_ordered * small_set_price
elif set_size == "big":
    total_cost = 5 * sets_ordered * large_set_price
discount = 0
if 400 <= total_cost <= 1000:
    discount = 0.15
elif total_cost > 1000:
    discount = 0.5
total_cost_with_discount = total_cost * (1 - discount)
print(f"{total_cost_with_discount :.2f} lv.")
