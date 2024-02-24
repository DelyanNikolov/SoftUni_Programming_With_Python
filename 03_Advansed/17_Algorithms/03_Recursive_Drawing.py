def recursion_drawing(num):
    if num == 0:
        return

    print("*" * num)

    recursion_drawing(num - 1)
    print("#" * num)


num = int(input())
recursion_drawing(num)
