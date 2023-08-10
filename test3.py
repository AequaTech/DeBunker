import spacy
import sys
from collections import Counter
nlp = spacy.load("it_core_news_lg")
doc = nlp("Si rifiuta tre volte di andare in una casa di riposo senza i suoi gatti e la struttura inaugura un piccolo rifugio per accoglierli")
i=0
j=sys.float_info.epsilon #avoid division by 0

#for token in doc._.abbreviations:
#    print(token)
for sent in doc.sents:
    if '?' in sent.text:
        print(sent)
    for token in sent:
        print(token.text,token.pos_,token.tag_,token.dep_,spacy.explain(token.pos_),spacy.explain(token.pos_),spacy.explain(token.tag_),token.morph,token.morph.to_dict())
        if 'Persons' in token.morph.to_dict():
            #j += 1
            if token.morph.to_dict()['Person']=='1' or token.morph.to_dict()['Person']=='2':
                #i+=1
                ...

        if token.pos_=='ADJ':
            j+=1
            if 'Degree' in token.morph.to_dict():
                i += 1


        if token.pos_=='ADJ' or token.pos_=='NOUN':
            j+=1
            if 'mod' in token.dep_:
                i += 1

        if token.pos_=='NUM':
            j+=1
            if 'mod' in token.dep_:
                i += 1
print(i,j,i/j)