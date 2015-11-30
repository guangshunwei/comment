import codecs


def df_wirte_to_file(filename, feature, sample):
    fw = codecs.open(filename, 'w', 'gbk')
    for word in feature:
        count = 0
        for s in sample:
            if word in s:
                count += 1
        fw.write(word)
        fw.write('\t')
        fw.write(count)
        fw.write('\n')
    fw.close()


import math


def write_weight(filename, feature, sample, count_list, classLabel, N):
    fw = open(filename, 'w')
    for word_list in sample:
        length = len(word_list)
        fw.write(str(classLabel))
        fw.write(' ')
        for word in feature:
            if word in word_list:
                cnt = word_list.count(word)
                tf = cnt / float(length)
                df = count_list[word_list.index(word)]
                idf = math.log(N/float(int(df)+1))
                feature_value = tf*idf
                fw.write(str(feature.index(word)) + ':' + str(feature_value) + ' ')
            else:
                feature_value = 0
                fw.write(str(feature.index(word)) + ':' + str(feature_value) + ' ')
        fw.write('\n')
    fw.close()
