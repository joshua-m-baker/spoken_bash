import re

files = [
    ("2D5LDCQ7B", r"^> "),
    ("4P8HWPCXV", r"^## "),
    ("586AC4KKQ", r"^# ?"),
    ("CU7MEACNU", r"^ \d\d\d\d ? ?"),
    ("HEHNDF7HP", r"^# "),
    ("FKUSU7EMJ", r".^"), 
]

results = {}

for (file_name, command_prefix) in files:
    f_path = 'raw_data/{}.txt'.format(file_name)

    with open(f_path) as f:
        current = ''
        for line in f.readlines():
            line = line.rstrip()
            if line:
                if re.match(command_prefix, line):
                    current = re.sub(command_prefix, '', line)
                    if current not in results.keys():
                        results[current] = []

                else:
                    if current!='':
                        results[current].append(line)

                    else:
                        command, spoken = line.split('\t')
                        if command not in results.keys():
                            results[command] = []
                        results[command].append(spoken)

with open("data/commands.txt", "w") as commands_file:
    with open("data/spoken.txt", "w") as spoken_file:

        for command, spoken_list in results.items():
            for spoken in spoken_list:

                commands_file.write(command)
                commands_file.write("\n")
                spoken_file.write(spoken)
                spoken_file.write("\n")
