
fuel_type = str(input())
fuel_amount = float(input())

if fuel_type == "Diesel":
    if fuel_amount < 25:
        print(f"Fill your tank with diesel!")
    else:
        print(f"You have enough diesel.")
elif fuel_type == "Gasoline":
    if fuel_amount < 25:
        print(f"Fill your tank with gasoline!")
    else:
        print(f"You have enough gasoline.")
elif fuel_type == "Gas":
    if fuel_amount < 25:
        print(f"Fill your tank with gas!")
    else:
        print(f"You have enough gas.")

else:
    print("Invalid fuel!")
