input_lines_count = int(input())
periodic_table = set()
for _ in range(input_lines_count):
    current_elements = set(input().split())
    periodic_table.update(current_elements)

for item in periodic_table:
    print(item)
