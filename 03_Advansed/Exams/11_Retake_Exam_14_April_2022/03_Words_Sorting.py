def words_sorting(*words):
    result = []
    words_data = {}
    sum_of_values = 0
    for current_word in words:
        ascii_sum = 0
        for letter in current_word:
            ascii_sum += ord(letter)
        words_data[current_word] = ascii_sum
        sum_of_values += ascii_sum
    if sum_of_values % 2 == 0:
        for word, value in sorted(words_data.items(), key=lambda x: x[0]):
            result.append(f"{word} - {value}")
    else:
        for word, value in sorted(words_data.items(), key=lambda x: -x[1]):
            result.append(f"{word} - {value}")

    return '\n'.join(result)


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
