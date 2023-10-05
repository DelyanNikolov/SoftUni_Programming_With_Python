def check_who_won(a):

    win = False
    if first_line.count(a) > 2 or second_line.count(a) > 2 or third_line.count(a) > 2:
        win = True
    for index in range(len(first_line) - 1):
        if first_line[index] == a and second_line[index] == a and third_line[index] == a:
            win = True
    if first_line[0] == a and second_line[1] == a and third_line[2] == a:
        win = True
    elif first_line[2] == a and second_line[1] == a and third_line[0] == a:
        win = True
    if win:
        return True


first_line = input().split(" ")
second_line = input().split(" ")
third_line = input().split(" ")

if check_who_won("1"):
    print("First player won")
elif check_who_won("2"):
    print("Second player won")
else:
    print("Draw!")
