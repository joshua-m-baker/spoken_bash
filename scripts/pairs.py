

with open("data/commands.txt") as commands_file, open("data/spoken.txt") as spoken_file: 
    for c, s in zip(commands_file, spoken_file):
        command = c.strip()
        spoken = s.strip()

        print("{} _ {}".format(command, spoken))
        print()
