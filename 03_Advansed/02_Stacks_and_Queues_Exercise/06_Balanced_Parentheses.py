# not my solution, mine is ugly and complex
parentheses_string = input()
parentheses_stack = []
ps = {
    '{': '}',
    '[': ']',
    '(': ')'
}

for item in parentheses_string:
    if item in ps:
        parentheses_stack.append(item)
    elif item in ps.values():
        if not parentheses_stack or ps[parentheses_stack.pop()] != item:
            print("NO")
            break
else:
    print("YES")
