#coding:gbk


import jieba
import codecs
import re

def ignore(s):
    return s == '，'.decode('gbk') or s == ' '.decode('gbk') or s == ' '.decode('gbk') or s == '/t'.decode('gbk') or s == '/n'.decode('gbk') \
           or s == '，'.decode('gbk') or s == '。'.decode('gbk') or s == '！'.decode('gbk') or s == '、'.decode('gbk') or s == '―'.decode('gbk')\
           or s == '？'.decode('gbk')  or s == '＠'.decode('gbk') or s == '：'.decode('gbk') \
           or s == '＃'.decode('gbk') or s == '%'.decode('gbk')  or s == '＆'.decode('gbk') \
           or s == '（'.decode('gbk') or s == '）'.decode('gbk') or s == '《'.decode('gbk') or s == '》'.decode('gbk') \
           or s == '［'.decode('gbk') or s == '］'.decode('gbk') or s == '｛'.decode('gbk') or s == '｝'.decode('gbk') \
           or s == '*'.decode('gbk') or s == ','.decode('gbk') or s == '.'.decode('gbk')  or s == '&'.decode('gbk') \
           or s == '!'.decode('gbk') or s == '?'.decode('gbk') or s == ':'.decode('gbk') or s == ';'.decode('gbk')\
           or s == '-'.decode('gbk') or s == '&'.decode('gbk')\
           or s == '<'.decode('gbk') or s == '>'.decode('gbk') or s == '('.decode('gbk') or s == ')'.decode('gbk') \
           or s == '['.decode('gbk') or s == ']'.decode('gbk') or s == '{'.decode('gbk') or s == '}'.decode('gbk') or s == 'nbsp10'.decode('gbk') or s == '3.6'.decode('gbk') or s=='about'.decode('gbk') or s =='there'.decode('gbk') \
           or s == "see".decode('gbk') or s == "can".decode('gbk') or s == "U".decode('gbk') or s == "L".decode('gbk') or s == " ".decode('gbk') or s == "in".decode('gbk') or s ==";".decode('gbk') or s =="a" or s =="0144"\
           or s == "\n" or s == "our" or s == '！'.decode('gbk') or s == '~'.decode('gbk') or s =='我'.decode('gbk')\
           or s =='你'.decode('gbk') or s =='它'.decode('gbk') or s =='他'.decode('gbk') or s == '了'.decode('gbk')\
           or s == '·'.decode('gbk') or s == '～'.decode('gbk') or s == '+' or s == '7'  or s == '70' or s == '╯'.decode('gbk')

# 载入数据并分词
def load_data(filename):
    classLabel = []
    sample = []
    fr = open(filename)
    lines = fr.readlines()
    for line in lines:
        if line != '\n':
            str = line.strip().split('\t')
            classLabel.append(str[1])
            str_split = jieba.cut(str[0])
            word_list = []
            for str_word in str_split:
                if ignore(str_word) == False:
                    word_list.append(str_word)
            sample.append(word_list)
    return sample, classLabel


def writ_to_file(filename, sample):
    fw = codecs.open(filename, 'a','utf-8')
    for i in range(len(sample)):
        for j in range(len(sample[i])):
            fw.write(sample[i][j])
            if(j != len(sample[i])-1):
                fw.write(' ')
        fw.write('\n')

s1, c1 = load_data('10point.txt')
s2, c2 = load_data('50point.txt')
length1 = len(s1)
length2 = len(s2)
target1 = int(length1*0.1)
target2 = int(length2*0.1)

writ_to_file('test10.txt', s1[0:target1], c1[0:target1])
writ_to_file('test50.txt', s2[0:target2], c2[0:target2])
writ_to_file('train10.txt', s1[target1+1:length1], c1[target1+1:length1])
writ_to_file('train50.txt', s2[target2+1:length2], c2[target2+1:length2])




