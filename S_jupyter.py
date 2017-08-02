
#-*- coding:utf-8 -*-
from wordcloud import WordCloud

import matplotlib.pyplot as plt
import os


font = "/Library/Fonts/华文细黑.ttf"
filename = '123.txt'
with open(filename) as f:
    mytext = f.read()


wordcloud = WordCloud(font_path=font).generate(mytext)
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.show()
