morse_code_dictionary = {'..-.': 'F', '-..-': 'X',
                         '.--.': 'P', '-': 'T', '..---': '2',
                         '....-': '4', '-----': '0', '--...': '7',
                         '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
                         '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
                         '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
                         '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
                         '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
                         '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1'}

words = [word.strip() for word in input().split(' | ')]
decrypted_message = []
for word in words:
    decrypted_word = ""
    letters = word.split(" ")
    for letter in letters:
        decrypted_word += morse_code_dictionary[letter]
    decrypted_message.append(decrypted_word)
print(" ".join(decrypted_message))
