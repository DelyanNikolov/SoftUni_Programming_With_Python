text = input().split()
result = ""
for i in range(len(text)):
    result += text[i] * len(text[i])
print(result)
