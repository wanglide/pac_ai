# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 18:49:57 2017

@author: April
"""
import thulac 
import simplejson as json
thu1 = thulac.thulac()  #默认模式
text = thu1.cut("我爱北京天安门", text=True)  #进行一句话分词
print(text)
emotionData=open('emotion.txt','r').read()
qinggan_dict = json.loads(emotionData)
print(qinggan_dict)
wordslist = text.split(' ')
qinggan_words = [];
for ix in wordslist:
     qinggan_words.append(ix.split('_'))
print(qinggan_words)
count = 0;
for ix in qinggan_words:
     if(ix[0] in qinggan_dict):
          count+=qinggan_dict[ix[0]]
