def is_word_palindrome(wrd):
    if wrd == wrd[::-1]:
        return True
    return False


words = input().split()
word = input()
palindrome = [word for word in words if is_word_palindrome(word)]
palindrome_count = words.count(word)
print(palindrome)
print(f"Found palindrome {palindrome_count} times")
