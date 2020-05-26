import io
import time
import os
from textblob import TextBlob

command_file = "/Users/rijinmk/Dropbox/RED-MALUS/commands.txt"

print(len("19+2+7+3+8+4+9+5+13+6+5+7+6+8+4+9+10+10+14+11+11+12+7+13+8+14+6+15+16+16+15+17+10+18+17+19+9+20+12+21+8".split("+")))

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