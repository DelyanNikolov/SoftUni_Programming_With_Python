available_cars = {}
cars_n = int(input())
for _ in range(cars_n):
    new_car = input().split("|")
    model = new_car[0]
    mileage = int(new_car[1])
    fuel = int(new_car[2])
    available_cars[model] = {'mileage': mileage, 'fuel': fuel}
# print(available_cars)

while True:
    command = input().split(" : ")
    if command[0] == "Stop":
        break
    elif command[0] == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel_spent = int(command[3])
        if available_cars[car]['fuel'] >= fuel_spent:
            available_cars[car]['mileage'] += distance
            available_cars[car]['fuel'] -= fuel_spent
            print(f"{car} driven for {distance} kilometers. {fuel_spent} liters of fuel consumed.")
            if available_cars[car]['mileage'] >= 100_000:
                available_cars.pop(car)
                print(f"Time to sell the {car}!")
        else:
            print("Not enough fuel to make that ride")
    elif command[0] == "Refuel":
        car = command[1]
        fuel_to_add = int(command[2])
        fuel_added = min(fuel_to_add, 75 - available_cars[car]['fuel'])
        available_cars[car]['fuel'] += fuel_added
        print(f"{car} refueled with {fuel_added} liters")
    elif command[0] == "Revert":
        car = command[1]
        kilometers = int(command[2])
        available_cars[car]['mileage'] -= kilometers
        if available_cars[car]['mileage'] < 10_000:
            available_cars[car]['mileage'] = 10_000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

for car, info in available_cars.items():
    print(f"{car} -> Mileage: {info['mileage']} kms, Fuel in the tank: {info['fuel']} lt.")
