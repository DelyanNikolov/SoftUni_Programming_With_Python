some_text = input()
some_text_list = [char for char in some_text]
for _ in some_text:
    print(some_text_list.pop(), end="")
