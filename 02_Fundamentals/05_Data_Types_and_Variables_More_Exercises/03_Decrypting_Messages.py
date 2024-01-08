key = int(input())
symbols_count = int(input())
decrypted_msg = ""

for _ in range(symbols_count):
    symbol = ord(input())
    decrypted_symbol = chr(symbol + key)
    decrypted_msg += decrypted_symbol

print(decrypted_msg)
