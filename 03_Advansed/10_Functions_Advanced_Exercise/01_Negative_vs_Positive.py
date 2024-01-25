def negative_positive(nums):
    negative_sum = sum(int(num) for num in nums if num < 0)
    positive_sum = sum(int(num) for num in nums if num > 0)
    print(negative_sum)
    print(positive_sum)

    if abs(negative_sum) < positive_sum:
        return f"The positives are stronger than the negatives"
    else:
        return f"The negatives are stronger than the positives"


numbers = [int(x) for x in input().split()]
print(negative_positive(numbers))
