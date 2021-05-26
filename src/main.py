import sys

# Change to false to have it read from cmd prompt input (normal use)
dev = False

to_open = "program.txt" if dev else sys.argv[1]

content = None

with open(to_open, "r") as f:
    content = [i.rstrip("\n") for i in f.readlines()]

helper = {"F": "if", "E": "else", "I": "elif", "q": "==", "M": ">", "L": "<", "m": ">=", "l": "<=", "n": "in", "o": "not", "a": "=", "p": "(", "P": ")", "b": "[", "B": "]", "d": "and", "r": "or", "u": "+", "i": "-", "v": "/", "k": "*", "K": "%", "w": "int", "W": "str", "O": "float", "h": "list", "H": "set", "t": "True", "f": "False", "N": "None", "c": ",", "z": " ", "s": "+=", "x": "-=", "U": "\"", "T": "print", "D": "def", "g": "input", "y": "for", "Y": "range", "j": "len", "J": ":"}

file = open("randomnameforthis.py", "w+")

for line in content:
    is_cond = False
    char = 0
    while char < len(line):
        if line[char] == " ":
            file.write("\t")
        elif line[char] == "V":
            temp = line[char + 1:]
            file.write(temp[:temp.index("V")])
            char += len(temp[:temp.index("V")]) + 1
        elif line[char] in "1234567890.":
            file.write(line[char])
        else:
            if line[char] == "F" or line[char] == "E" or line[char] == "I" or line[char] == "D" or line[char] == "y:
                is_cond = True
            file.write(helper[line[char]])
        char += 1

    if is_cond:
        file.write(":\n")
    else:
        file.write("\n")

file.close()
