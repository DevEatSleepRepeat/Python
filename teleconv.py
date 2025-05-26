import os
def astelevals(text):
    if text == "a" or text == "b" or text == "c":
        return 2
    if text == "d" or text == "e" or text == "f":
        return 3
    if text == "g" or text == "h" or text == "i":
        return 4
    if text == "j" or text == "k" or text == "l":
        return 5
    if text == "m" or text == "n" or text == "o":
        return 6
    if text == "p" or text == "q" or text == "r" or text == "s":
        return 7
    if text == "t" or text == "u" or text == "v":
        return 8
    if text == "w" or text == "x" or text == "y" or text == "z":
        return 9
def asflipvals():
    flipconvt = {
        "a":"2",
        "b":"22",
        "c":"222",
        "d":"3",
        "e":"33",
        "f":"333",
        "g":"4",
        "h":"44",
        "i":"444",
        "j":"5",
        "k":"55",
        "l":"555",
        "m":"6",
        "n":"66",
        "o":"666",
        "p":"7",
        "q":"77",
        "r":"777",
        "s":"7777",
        "t":"8",
        "u":"88",
        "v":"888",
        "w":"9",
        "x":"99",
        "y":"999",
        "z":"9999"
    }
    return flipconvt
def flipconvt(text):
    fvals = asflipvals()
    output = ""
    for i in range(0,len(text)):
        output += fvals[text[i]]
    return output

def teleconvt(text):
    output = ""
    for i in range(0,len(text)):
        output += astelevals(text[i])
    return output

def main():
    print("Welcome to Sam's Telephone number converter!\nChoose a Converter:\n[1] Text to Telephone Keypad\n[2] Flip Phone Input Converter\nor\n[0] Quit")
    inp = input(">>> ")
    if inp == "1":
        os.system("clear")
        inptext = input("Enter the text you want converted:\n>>> ")
        print("\nYour Converted Number is "+teleconvt(inptext))

main()