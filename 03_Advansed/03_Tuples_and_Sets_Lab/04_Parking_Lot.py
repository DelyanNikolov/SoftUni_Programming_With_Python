n = int(input())
parking_lot = set()

for car in range(n):
    command, license_plate = input().split(", ")
    if command == "IN":
        parking_lot.add(license_plate)
    elif command == "OUT":
        parking_lot.remove(license_plate)

if parking_lot:
    for car in parking_lot:
        print(car)
else:
    print("Parking Lot is Empty")
