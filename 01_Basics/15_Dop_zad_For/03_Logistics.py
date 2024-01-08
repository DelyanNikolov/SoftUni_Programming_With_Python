cargo_count = int(input())

bus_cargos = 0
truck_cargos = 0
train_cargos = 0
middle_price = 0

total_cargo = 0
for _ in range(cargo_count):
    cargo_weight_tons = int(input())
    total_cargo += cargo_weight_tons
    if cargo_weight_tons <= 3:
        bus_cargos += cargo_weight_tons
    elif cargo_weight_tons <= 11:
        truck_cargos += cargo_weight_tons
    elif cargo_weight_tons >= 12:
        train_cargos += cargo_weight_tons

middle_price = (bus_cargos * 200 + truck_cargos * 175 + train_cargos * 120) / total_cargo

bus_cargos_percentage = bus_cargos / total_cargo * 100
truck_cargos_percentage = truck_cargos / total_cargo * 100
train_cargos_percentage = train_cargos / total_cargo * 100

print(f"{middle_price:.2f}")
print(f"{bus_cargos_percentage:.2f}%")
print(f"{truck_cargos_percentage:.2f}%")
print(f"{train_cargos_percentage:.2f}%")
