import codecs


def read_feature(filename):
    feature = []
    fr = codecs.open(filename, 'r', 'gbk')
    lines = fr.readlines()
    for line in lines:
        feature.append(line.strip())
    fr.close()
    return feature


def read_idf(filename):
    word_list = []
    count_list = []

    fr = open(filename, 'r')
    lines = fr.readlines()
    for line in lines:
        str = line.strip().split('\t')
        word_list.append(str[0])
        count_list.append(str[1])
    return word_list, count_list
