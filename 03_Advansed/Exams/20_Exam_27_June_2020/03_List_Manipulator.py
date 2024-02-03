from collections import deque


def list_manipulator(numbers, command_1, command_2, *args):
    list_result = deque(numbers)
    if command_1 == "remove":
        if command_2 == "end":
            if not args:
                list_result.pop()
            else:
                for _ in range(args[0]):
                    list_result.pop()
        elif command_2 == "beginning":
            if not args:
                list_result.popleft()
            else:
                for _ in range(args[0]):
                    list_result.popleft()
    elif command_1 == "add" and command_2 == "beginning":
        for i in range(len(args) - 1, -1, -1):
            list_result.appendleft(args[i])
    elif command_1 == "add" and command_2 == "end":
        for i in range(len(args)):
            list_result.append(args[i])
    return list(list_result)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
