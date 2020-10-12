import bashlex

with open("data/cd_commands.txt") as f:
    with open("data/cd_command_tokens.txt", 'w') as output:
        for line in f.readlines():
            try:
                output.write(" ".join(bashlex.split(line)))
            except:
                output.write(line)
