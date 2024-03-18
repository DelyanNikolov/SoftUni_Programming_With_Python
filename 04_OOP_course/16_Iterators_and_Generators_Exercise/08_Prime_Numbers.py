from math import isqrt


def get_primes(sequence):
    for num in sequence:
        if num <= 1:
            continue

        for divisor in range(2, isqrt(num) + 1):
            if num % divisor == 0:
                break
        else:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))