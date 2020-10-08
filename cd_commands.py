import re


file_name = "raw_data/cd_full.txt"
command_prefix = r"^ +\d+ +"

replacements = {
    " ": ["", "space"],
    "/": ["slash", "forward slash"],
    "-": ["dash", "hyphen"],
    ".": ["dot"],
    "_": ["under score", "underscore"],
    "~": ["tilde", "squiggle", "home"],
    "|": ["pipe", "bar"],
    '"': ["quote", "quotation"],
    "'": ["quote", "quotation"],
    ">": ["into", "carrot", "greater than"],
    "cd": ["cd", "c d"],
}

commands = {}

with open(file_name) as f:
    current = ''
    for line in f.readlines():
        line = line.rstrip()
        if line:
            if re.match(command_prefix, line):
                command = re.sub(command_prefix, '', line)
                if command not in commands.keys():
                    commands[command] = []
                    
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
    # for command in transformed:

#print(commands)


            

with open("data/cd_commands.txt", "w") as commands_file:
    with open("data/cd_spoken.txt", "w") as spoken_file:

        for command, spoken_list in commands.items():
            for spoken in spoken_list:

                commands_file.write(command)
                commands_file.write("\n")
                spoken_file.write(spoken)
                spoken_file.write("\n")
