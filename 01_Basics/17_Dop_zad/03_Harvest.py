import math

x_square_meters_vines = int(input())
y_grapes_for_square_meter = float(input())
z_liters_wine_needed = int(input())
workers_count = int(input())

square_meters_for_wine = x_square_meters_vines * 0.4
kilograms_grapes_produced = square_meters_for_wine * y_grapes_for_square_meter
liters_wine_produced = kilograms_grapes_produced / 2.5
wine_left = abs(z_liters_wine_needed - liters_wine_produced)
wine_per_worker = math.ceil(wine_left / workers_count)

if liters_wine_produced < z_liters_wine_needed:
    print(f"It will be a tough winter! More {math.floor(wine_left)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(liters_wine_produced)} liters.\n"
          f"{math.ceil(wine_left)} liters left -> {wine_per_worker} liters per person.")
