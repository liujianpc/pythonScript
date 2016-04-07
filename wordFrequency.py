#! /usr/bin/env python
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
strDemo = "what is a fuck test, this test is fuck, and a good test is good fuck."
wordList = strDemo.split(None)
wordList2 = []
for word in wordList:
    
    if word[-1] in [',','.',';',':','?','/']:
        wordTemp = word.rstrip(word[-1])
    else:
        wordTemp = word
    wordList2.append(wordTemp)

wordDict = {}
for word2 in wordList2:
    wordDict[word2] = wordDict.get(word2,0) + 1

keys = wordDict.keys()
keys.sort()
for key in keys:
    print key+":"+ str(wordDict[key])
    
        
    
    