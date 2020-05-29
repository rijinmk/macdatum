from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize 

ps = PorterStemmer()

example_words = ["Pythoning", "Pythoner", "Pythoning", "Pythonly"]

for i in example_words: 
    print(ps.stem(i))