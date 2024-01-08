meters_to_top = 5364
days_climbing = 1
success = False
command = input()
while command != "END":
    if command == "Yes":
        days_climbing += 1
    meters_climbed = int(input())
    if days_climbing <= 5:
        meters_to_top += meters_climbed
    if meters_to_top >= 8848:
        success = True
        break
    if days_climbing > 5:
        break
    command = input()
if success:
    print(f"Goal reached for {days_climbing} days!")
else:
    print("Failed!")
    print(f"{meters_to_top}")
