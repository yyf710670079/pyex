#! /usr/bin/env python3#  -*- coding: utf-8 -*-import randomspeechPartsDict={}#构造词性字典def add_speechPart(partType,fileName):    """ 从含有某种词性partType的单词的文件fileName中，读取其中的单词，加到在词性字典"""	#你的代码写在后面    with open(fileName,'r')as f:        line=f.readline()        line=line.split(',')        speechPartsDict[partType]=linedef makeOneSentence(sentencePattern):    """ 按照输入的句子结构构造一个句子，并返回该句子"""	#你的代码写在后面    pattern_list=sentencePattern.split(' ')    new_sentence=[]    for i in pattern_list:        if i in speechPartsDict.keys():            new_sentence.append(\                speechPartsDict[i][random.randint(0,len(speechPartsDict[i])-1)])        else:            new_sentence.append(i)    new_sentence=' '.join(new_sentence)    return new_sentencedef main():    add_speechPart("adj","adj.txt")    add_speechPart("noun","noun.txt")    add_speechPart("verb","verb.txt")    print(speechPartsDict)    sentencePattern ="The adj noun verb ."	#你的代码写在后面    while True:        num_sentence=input('请输入需要创建的句子数目:')        try:            num_sentence=int(num_sentence)        except ValueError:            print('你输入有误，请重新输入...')        else:            break    for j in range(num_sentence):        print('{0:,}. {1:}'.format(j+1,makeOneSentence(sentencePattern)))if __name__ == '__main__':    main()