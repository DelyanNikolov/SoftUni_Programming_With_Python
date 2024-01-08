# Фигурите са четири вида: квадрат (square), правоъгълник (rectangle), кръг (circle) и триъгълник (triangle). На първия ред на входа се чете вида на фигурата (текст със следните възможности: square, rectangle, circle или triangle).
# •	Ако фигурата е квадрат (square): на следващия ред се чете едно дробно число - дължина на страната му
# •	Ако фигурата е правоъгълник (rectangle): на следващите два реда четат две дробни числа - дължините на страните му
# •	Ако фигурата е кръг (circle): на следващия ред чете едно дробно число - радиусът на кръга
# •	Ако фигурата е триъгълник (triangle): на следващите два реда четат две дробни числа - дължината на страната му и дължината на височината към нея
# Резултатът да се закръгли до 3 цифри след десетичната запетая.
from math import pi

figure_type = input()
area = 0
if figure_type == "square":
    side = float(input())
    area = side * side
elif figure_type == "rectangle":
    first_side = float(input())
    second_side = float(input())
    area = first_side * second_side
elif figure_type == "circle":
    radius = float(input())
    area = pi * radius ** 2

elif figure_type == "triangle":
    side = float(input())
    height = float(input())
    area = side * height / 2
print(f"{area:.3f}")
