import io
import time
import os
from textblob import TextBlob

command_file = "/Users/rijinmk/Dropbox/RED-MALUS/commands.txt"

f_mod_o = os.path.getmtime(command_file)
while True:
    time.sleep(1)
    f_mod_n = os.path.getmtime(command_file)
    print("Time difference: ", f_mod_n - f_mod_o)
    
    f = open(command_file, 'r')
    last = f.readlines()[-1].strip()
    f.close()

    last = TextBlob(last)
    print(last.tags)

print(last)