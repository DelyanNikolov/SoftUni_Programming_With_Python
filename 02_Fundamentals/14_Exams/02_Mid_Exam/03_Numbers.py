list_of_numbers = [int(num) for num in input().split()]
average = sum(list_of_numbers) / len(list_of_numbers)
top_nums = [top for top in list_of_numbers if top > average]
top_nums.sort(reverse=True)
top_five_nums = top_nums[:5]

if top_nums:
    print(" ".join(map(str, top_five_nums)))
else:
    print("No")
