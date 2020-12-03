import re


file_name = "../raw_data/raw/raw_data_full.txt"
command_prefix = r"^ +\d+ +"

replacements = {
    " ": ["", "space"],
    "/": ["slash", "forward slash"],
    "-": ["dash", "hyphen"],
    ".": ["dot"],
    "_": ["under score", "underscore"],
    "~": ["tilde", "squiggle", "home"],
    "|": ["pipe", "bar"],
    '"': ["quote", "quotation", "double quote"],
    "'": ["quote", "quotation", "single quote"],
    ">": ["into", "carrot", "greater than"],
    "cd": ["cd", "c d"],
    "!": ["bang", "exclamation", "exclamation point"], 
    "@": ["at", "at symbol"],
    "%": ["percent", "percent symbol"],
    ":": ["colon"],
    ";": ["semicolon"],
    "(": ["left paren", "left parenthesis"],
    ")": ["right paren", "right parenthesis"],
    "`": ["tick", "backtick"],
    "#": ["pound", "hash", "hashtag"],
    "$": ["dollar", "dollar sign"],
    "^": ["up arrow", "up"],
    "&": ["and", "ampersand", "and symbol"],
    "*": ["star", "asterisk"],
    "+": ["plus", "plus sign"],
    "=": ["equals", "equals sign"],
    "0": ["zero", "o"],
    "1": ["one"],
    "2": ["two"],
    "3": ["three"],
    "4": ["four"],
    "5": ["five"],
    "6": ["six"],
    "7": ["seven"],
    "8": ["eight"],
    "9": ["nine"],
}

commands = {}
import bashlex

with open(file_name) as f:
    current = ''
    for line in f.readlines(): 
        line = line.rstrip()           
        try:
            tokens = " ".join(bashlex.split(line))

            if tokens not in commands.keys():
                commands[tokens] = []
        except Exception as e:
            print(e)
            continue
                    
for c in commands.keys():

    transformed = [c]
        
    for symbol, words in replacements.items():

        new_transformed = []

        for replacement in words:

            for t in transformed:
                if symbol in t:
                    
                    new = t.replace(symbol, f" {replacement} ")
                    new = re.sub(' +', ' ', new)
                    new_transformed.append(new)

        transformed = new_transformed or transformed

    commands[c] = transformed

with open("../data/tgt-full-train.txt", "w") as commands_file:
    with open("../data/src-full-train.txt", "w") as spoken_file:

        for command, spoken_list in commands.items():
            for spoken in spoken_list:

                commands_file.write(command.strip())
                commands_file.write("\n")
                spoken_file.write(spoken.strip())
                spoken_file.write("\n")
