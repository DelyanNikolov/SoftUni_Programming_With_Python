side = int(input())
matrix = [[int(el) for el in input().split(", ")] for row in range(side)]

primary_diagonal = [matrix[x][x] for x in range(side)]
secondary_diagonal = [matrix[x][side-x-1] for x in range(side)]


print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
