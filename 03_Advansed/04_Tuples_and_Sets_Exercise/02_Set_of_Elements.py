n, m = (input()).split()

set_a = set()
set_b = set()

for num in range(int(n) + int(m)):
    number = int(input())
    if num < int(n):
        set_a.add(number)
    else:
        set_b.add(number)
set_c = set_a.intersection(set_b)
for num in set_c:
    print(num)