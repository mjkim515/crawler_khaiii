# -*- coding: utf-8 -*-

#===============================================================================
#
#  Test Method : python word_word2vec_test.py [input modelname] [keword]
#  
#  ex) python word_word2vec_test.py donga.model  word
#
#===============================================================================


import sys

import matplotlib.pyplot as plt
from matplotlib import rc



from gensim.models import word2vec

# Apple MacOS
plt.rc('font', family='AppleGothic')


def showGraph(bargraph, inputword):

     xtick = [item[0] for item in bargraph] 

     ytick = [item[1] for item in bargraph] 

     plt.figure()

     mycolors = ['#06c2ac', '#06c2ac', '#c79fef','#c79fef', '#ff796c', '#ff796c', \
                 '#aaff32', '#aaff32', '#0485d1', '#0485d1', '#a5a502', '#a5a502']
                 
     title = model_filename + " [ " + inputword + " ] 연관어 검출 결과"
     plt.title(title)
     plt.bar(xtick, ytick, color=mycolors)




model_filename = sys.argv[1] #'hani.model'

model = word2vec.Word2Vec.load(model_filename)

inputword = sys.argv[2] 
print("Model Name : " + model_filename + "Input keyword : ", inputword)



bargraph = model.wv.most_similar(positive=[inputword])

showGraph(bargraph, inputword)

#similarity_test = []
#similarity_test = model.wv.similarity('후보', '후보자')
#
#print ("사업 : " + str(similarity_test))

plt.show()

