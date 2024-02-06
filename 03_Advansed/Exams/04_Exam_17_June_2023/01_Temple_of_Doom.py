from collections import deque

tools = deque(int(x) for x in input().split())
substances_stack = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]


while challenges:
    if substances_stack and tools:
        tool = tools.popleft()
        substance = substances_stack.pop()
        result = substance * tool
        if result in challenges:
            challenges.pop(challenges.index(result))
        else:
            tool += 1
            tools.append(tool)
            substance -= 1
            if substance > 0:
                substances_stack.append(substance)
    else:
        break

if (not substances_stack or tools) and challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
elif not challenges:
    print(f"Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join(map(str, tools))}")
if substances_stack:
    print(f"Substances: {', '.join(map(str, substances_stack))}")
if challenges:
    print(f"Challenges: {', '.join(map(str, challenges))}")
