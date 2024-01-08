NYLON = 1.50
PAINT = 14.50
DILUENT = 5.00
BAGS = 0.40

required_nylon = int(input())
required_paint = int(input())
required_diluent = int(input())
required_time = int(input())


nylon_price = (required_nylon + 2) * NYLON
paint_price = (required_paint+ required_paint * 0.1) * PAINT
diluent_price = required_diluent * DILUENT

work_price = (nylon_price + paint_price + diluent_price + BAGS) * 0.3

total_cost_price = nylon_price + paint_price + diluent_price + BAGS + work_price * required_time

print(total_cost_price)