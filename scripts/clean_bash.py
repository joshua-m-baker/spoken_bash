

command_prefix = r"^ *\d+ +"

files = ["history1", "history2", "history5", "history3", "history4"]

import bashlex
import re

with open("raw_data_full.txt", 'w') as out:
    for fname in files:

        with open(f"{fname}.txt") as f:
    
            for line in f.readlines():
                line = line.rstrip()
                if line:
                    try:
                        command = re.sub(command_prefix, '', line)
                        bashlex.split(command)
                        out.write(f"{command}\n")
                    except Exception as e:
                        print(e)
                        continue
