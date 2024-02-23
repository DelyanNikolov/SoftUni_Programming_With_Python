from pyfiglet import figlet_format


def print_text_art(msg):
    text_art = figlet_format(msg)
    print(text_art)


print_text_art(input())
