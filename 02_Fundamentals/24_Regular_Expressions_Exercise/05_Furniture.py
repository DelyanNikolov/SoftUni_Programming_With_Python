import re


def check_valid_purchase(info):
    result = re.findall(pattern, info)
    if result:
        return True
    return False


def extract_information(info):
    """this function use regex to separate item name, item price and item quantity"""
    result = re.search(pattern, info)
    item_name, item_price, item_quantity = result.groups()
    return item_name, float(item_price), int(item_quantity)


def store_data(item_name: str):
    """storing item name and total price to a dictionary for later print"""
    furniture.append(item_name)


furniture = []
total_cost = 0
pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)\!(\d+)"

while True:
    # starting collecting data for purchases
    purchase_info = input()

    # the command "Purchase" ends the collection of data
    if purchase_info == "Purchase":
        break

    # check if the input is valid
    if check_valid_purchase(purchase_info):
        # taking name, price, quantity
        name, price, quantity = extract_information(purchase_info)
        # store item name and add price to total
        store_data(name)
        total_cost += price * quantity

# printing final result:
print("Bought furniture:")
for item in furniture:
    print(f"{item}")
print(f"Total money spend: {total_cost:.2f}")
