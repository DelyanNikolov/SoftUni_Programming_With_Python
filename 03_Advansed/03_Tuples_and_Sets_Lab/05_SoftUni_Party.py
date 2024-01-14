n = int(input())
guests = set()
for _ in range(n):
    code = input()
    guests.add(code)

command = input()
while command != "END":
    code = command
    if code in guests:
        guests.remove(code)
    command = input()
print(len(guests))
for item in sorted(guests):
    print(item)
