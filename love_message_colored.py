import pyfiglet
from termcolor import colored

def print_love_message():
    message = "I Love You, Faith Naswa"
    font = "slant"  # You can change the font to any available font in pyfiglet
    ascii_art = pyfiglet.figlet_format(message, font=font)
    colored_ascii_art = colored(ascii_art, 'blue')
    print(colored_ascii_art)

print_love_message()