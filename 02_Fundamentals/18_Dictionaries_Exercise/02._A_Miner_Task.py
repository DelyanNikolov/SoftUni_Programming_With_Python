resources = {}
while True:

    resource = input()
    if "stop" in resource:
        break
    quantity = int(input())
    if resource not in resources:
        resources[resource] = quantity
    else:
        resources[resource] += quantity

for res in resources:
    print(f"{res} -> {resources[res]}")
