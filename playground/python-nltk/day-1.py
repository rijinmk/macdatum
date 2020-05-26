from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

s = "Nandana is a dumbass and Rijin is a smart ass"
sw = set(stopwords.words("english"))
w = word_tokenize(s)
f = []
for i in w: 
    if i not in sw: 
        f.append(i)
print(' '.join(f))