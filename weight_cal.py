import read_data
import math


def write_weight(filename, feature, sample, word_list, count_list, classLabel, N):
    fw = open('train.txt', 'a')
    for word_list in sample:
        fw.write(classLabel)
        fw.write(' ')
        for word in feature:
            cnt = word_list.count(word)
            tf = cnt / float(word_list)
            df = count_list[word_list.index(word)]
            idf = math.log(N/float(df+1))
            feature_value = tf*idf
            fw.write(str(feature.index(word))+':'+str(feature_value)+' ')
        fw.write('\n')

