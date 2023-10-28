import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts=figlet.getFonts()

def main():
    if len(sys.argv)==1:
        font_name=random.choice(fonts)
    elif len(sys.argv)==3 and (sys.argv[1]=='-f' or sys.argv[1]=='--font'):
        font_name=sys.argv[2]
    else:
        print("Invalid usage")
        sys.exit(1)

    figlet=Figlet(font=font_name)

    if font_name:
        if font_name not in fonts:
            print("Font is not available")
            sys.exit(1)

    text = input("Input: ")
    output = figlet.renderText(text)
    print(output)

main()
