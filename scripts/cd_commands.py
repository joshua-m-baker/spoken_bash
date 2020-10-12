import re


file_name = "../raw_data/raw/cd_commands.txt"
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
    "(": ["parenthesis", "paren", "left paren", "left parenthesis"],
    "(": ["parenthesis", "paren", "right paren", "right parenthesis"],
    "`": ["tick", "backtick"]
}

commands = {}
import bashlex

with open(file_name) as f:
    current = ''
    for line in f.readlines():
        line = line.rstrip()
        if line:
            if re.match(command_prefix, line):
                command = re.sub(command_prefix, '', line)

                try:
                    tokens = " ".join(bashlex.split(command))

                    if tokens not in commands.keys():
                        commands[tokens] = []
                except:
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

with open("../data/tgt-cd-train.txt", "w") as commands_file:
    with open("../data/src-cd-train.txt", "w") as spoken_file:

        for command, spoken_list in commands.items():
            for spoken in spoken_list:

                commands_file.write(command)
                commands_file.write("\n")
                spoken_file.write(spoken)
                spoken_file.write("\n")
