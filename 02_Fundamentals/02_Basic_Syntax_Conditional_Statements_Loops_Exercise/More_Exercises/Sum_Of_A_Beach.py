key_words = ["sand", "water", "fish", "sun"]

search_string = input()
search_string = search_string.lower()
counter = 0
for item in key_words:
    results = search_string.count(item)
    if results > 0:
        counter += results
print(counter)
