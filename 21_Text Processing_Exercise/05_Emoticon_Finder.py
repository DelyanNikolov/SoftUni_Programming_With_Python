text = input()
for index in range(len(text)):
    emoticons = ""
    if text[index] == ":":
        emoticons += f":{text[index + 1]}"
        print(emoticons)
