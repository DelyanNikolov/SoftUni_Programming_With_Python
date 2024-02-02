import os
import re

words_path = os.path.join("exercise_files", "words.txt")
text_path = os.path.join("exercise_files", "input.txt")
output_path = os.path.join("exercise_files", "output.txt")

with open(words_path, "r") as words_file:
    searched_words_as_text = words_file.read()
    searched_words = [word.lower() for word in searched_words_as_text.split()]

with open(text_path, "r") as text_file:
    content = text_file.read().lower()

words_count = {}

for searched_word in searched_words:
    regex = re.compile(rf"\b{searched_word}\b")
    results = re.findall(regex, content)
    words_count[searched_word] = results.count(searched_word)

sorted_result = sorted(words_count.items(), key=lambda x: -x[1])

with open(output_path, "w") as output_file:  # write mode so in testing to create and re write file on every run
    for word, count in sorted_result:
        output_file.write(f"{word} - {count}\n")
