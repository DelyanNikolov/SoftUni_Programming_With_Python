from math import floor, sqrt


def nearest_to_center(p1, v1, p2, v2):
    distance_to_center_1 = abs(p1) ** 2 + abs(v1) ** 2
    distance_to_center_2 = abs(p2) ** 2 + abs(v2) ** 2
    if distance_to_center_1 > distance_to_center_2:
        print(f"({floor(p2)}, {floor(v2)})({floor(p1)}, {floor(v1)})")
    elif distance_to_center_1 < distance_to_center_2:
        print(f"({floor(p1)}, {floor(v1)})({floor(p2)}, {floor(v2)})")
    else:
        print(f"({floor(p1)}, {floor(v1)})({floor(p2)}, {floor(v2)})")


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    l1 = sqrt((abs((x1 - x2))**2 + abs((y1 - y2)) ** 2))
    l2 = sqrt((abs((x3 - x4))**2 + abs((y3 - y4)) ** 2))

    if l1 < l2:
        coordinates_longer_line = [x3, y3, x4, y4]
    else:
        coordinates_longer_line = [x1, y1, x2, y2]
    return coordinates_longer_line


k1 = float(input())
k2 = float(input())
k3 = float(input())
k4 = float(input())
k5 = float(input())
k6 = float(input())
k7 = float(input())
k8 = float(input())

coord = longer_line(k1, k2, k3, k4, k5, k6, k7, k8)
nearest_to_center(coord[0], coord[1], coord[2], coord[3])
