def create_sequence(n):
    seq = [0, 1]

    for _ in range(n - 2):
        next_num = seq[-1] + seq[-2]
        seq.append(next_num)
    print(*seq)


def locate_number(number, seq):
    pass
