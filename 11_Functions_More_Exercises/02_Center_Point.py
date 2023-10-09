from math import floor


def nearest_to_center(x1, y1, x2, y2):
    distance_to_center_1 = abs(x1) ** 2 + abs(y1) ** 2
    distance_to_center_2 = abs(x2) ** 2 + abs(y2) ** 2
    if distance_to_center_1 > distance_to_center_2:
        print(f"({floor(x2)}, {floor(y2)})")
    elif distance_to_center_1 < distance_to_center_2:
        print(f"({floor(x1)}, {floor(y1)})")
    else:
        print(f"({floor(x1)}, {floor(y1)})")


coordinate_x1 = float(input())
coordinate_y1 = float(input())

coordinate_x2 = float(input())
coordinate_y2 = float(input())
nearest_to_center(coordinate_x1, coordinate_y1, coordinate_x2, coordinate_y2)
