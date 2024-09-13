# -*- coding: utf-8 -*-
"""
The goal of this script was to parse through a large corpus of the Japanese langauge
in order to find differneces in language use between native speaker and second language speakers.
This project was done in collaboration with a graduate student in linguistics and a graduate student in psychology.



"""



# import needed libraries

import spacy
import os
#from spacy import displacy
import re
import pandas as pd



#load in all of the files
os.chdir("nani_and_ga")

allfiles = [file for file in os.listdir(os.getcwd()) if file[-4:] == ".txt" and file != "nani_and_ga_raw.txt"]


# create a new variable to hold the following information: 
sourceFile = []
text = []
lemma = []
pos = []
tag = []
dep = []
shape = []
isalpha = []
isstop = []
indexList = []

# load the japanese speech model
nlp = spacy.load("ja_core_news_trf")



# load file in; need to merge text files that all have the same cohort (will do later)


for file in allfiles:
    strings = ""
    index = 0
    with open (file, "r", encoding="utf8") as f: 
        for line in f:
            line = re.sub("\\u3000", " ",line).rstrip("\n\r")
        # append incoming strings to full text list 
            strings = strings + line       



# load the document we want to extract part of speech from 
    doc = nlp(strings)

# spacy: tags every word automatically!! tag for part of speech AND for extra credit, tag for the suffix itself 


# for each word in the doc, output the following: 

    for token in doc:
        if token.text != "|":
            index = index + 1
            indexList.append(index)
            sourceFile.append(file[:-4])
            text.append(token.text)
            lemma.append(token.lemma)
            pos.append(token.pos_)
            tag.append(token.tag_)
            dep.append(token.dep_)
            shape.append(token.shape_)
            isalpha.append(token.is_alpha)
            isstop.append(token.is_stop)
    
# Cobines everything into a dataframe for analysis 
results = pd.DataFrame(
    {'index': indexList,
     'source': sourceFile,
     'text': text,
#     'lemma': lemma,
     'pos': pos,
     'tag':tag,
     'dep':dep,
     'shape':shape,
     'isalpha':isalpha,
     'isstop':isstop

    })

# output to file 
results.to_csv(os.path.dirname(os.path.realpath(__file__))+"//naniga_combined_update.csv",sep=",",index = False, encoding='utf-16')

