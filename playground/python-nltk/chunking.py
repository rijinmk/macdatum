import nltk 
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

t = state_union.raw("2005-GWBush.txt")
s = state_union.raw("2006-GWBush.txt")
cst = PunktSentenceTokenizer(t)

tkn = cst.tokenize(s)

def process_content():
    try: 
        for i in tkn: 
            w = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(w)
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            chunked.draw()

    except Exception as e: 
        print("Error", e)

process_content()