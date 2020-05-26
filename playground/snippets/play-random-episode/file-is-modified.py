import time
import os 

command_file = "/Users/rijinmk/Dropbox/RED-MALUS/commands.txt"

h = [os.path.getmtime(command_file)]
while True: 
    time.sleep(1)
    h.append(os.path.getmtime(command_file))
    print(h[-1] - h[-2])

