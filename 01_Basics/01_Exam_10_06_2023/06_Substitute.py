k = int(input())
l = int(input())
m = int(input())
n = int(input())

combinations = 0
for K in range(k, 9):
    for L in range(9, l - 1, -1):
        for M in range(m, 9):
            for N in range(9, n - 1, -1):
                if K % 2 == 0 and M % 2 == 0 and L % 2 != 0 and N % 2 != 0:
                    if K == M and L == N:
                        print("Cannot change the same player.")
                        continue
                    print(f"{K}{L} - {M}{N}")
                    combinations += 1
                    if combinations >= 6:
                        exit()
