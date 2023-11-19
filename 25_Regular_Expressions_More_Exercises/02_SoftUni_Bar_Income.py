import re

pattern = re.compile(
    r"(%)(?P<customer>[A-Z][a-z]+)\1([^\|\$\%\.]*)"
    r"<(?P<product>[\w]+)>([^\|\$\%\.]*)"
    r"\|(?P<count>[\d]+)\|([^\|\$\%\.]*)"
    r"(?P<price>[1-9]+[.0-9]*)\$")
total_sum = 0
command = input()
while not command == "end of shift":
    result = re.finditer(pattern, command)
    for item in result:
        total_price = float(item["count"]) * float(item["price"])
        print(f"{item['customer']}: {item['product']} - {total_price:.2f}")
        total_sum += total_price
    command = input()
print(f"Total income: {total_sum:.2f}")
