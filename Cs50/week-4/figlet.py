import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
        figlet.setFont(font=font)
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        font = sys.argv[2]
        if font not in figlet.getFonts():
            sys.exit("Error: Font not found")
        figlet.setFont(font=font)
    else:
        sys.exit("Usage: figlet.py or figlet.py -f [fontname]")

    user_input = input("Enter a string: ")

    print(figlet.renderText(user_input))

if __name__ == "__main__":
    main()
