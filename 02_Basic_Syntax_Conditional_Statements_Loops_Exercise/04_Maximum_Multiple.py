# On the first line, you will be given a positive number, which will serve as a divisor.
# On the second line, you will receive a positive number that will be the boundary.
# You should find the largest integer N, that is:
# •	divisible by the given divisor
# •	less than or equal to the given bound
# •	greater than 0
# Note: it is guaranteed that N is found.
devisor = int(input())
boundary = int(input())
numbers = []
for n in range(1, boundary + 1):
    if n % devisor == 0:
        numbers.append(n)
print(max(numbers))
