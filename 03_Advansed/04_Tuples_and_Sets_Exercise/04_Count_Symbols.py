# sentence = input()
# characters = tuple(char for char in sentence)
# character_data = {}
# for char in characters:
#     count = characters.count(char)
#     character_data[char] = count
#
# for char, count in sorted(character_data.items()):
#     print(f"{char}: {count} time/s")
text = input()

for symbol in sorted(set(text)):
    print(f"{symbol}: {text.count(symbol)} time/s")
