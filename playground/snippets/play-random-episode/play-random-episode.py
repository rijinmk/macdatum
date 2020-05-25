import io
from textblob import TextBlob

f = open("/Users/rijinmk/Dropbox/RED-MALUS/commands.txt", 'r')
last = f.readlines()[-1].strip()
f.close()

print(last)