# coding:gbk
import codecs
import featureSelection
import read_data
import write_data

# 计算idf并写入idf.txt的命令
# ======================================================================
# feature = read_data.read_feature('feature.txt')
# word_set1, word_list1 = featureSelection.getClassDic('train10.txt')
# word_set2, word_list2 = featureSelection.getClassDic('train50.txt')

# word_list = []
# word_list.extend(word_list1)
# word_list.extend(word_list2)

# write_data.df_wirte_to_file('idf.txt', feature, word_list)
# ========================================================================


# 计算每个样本的特征weight，并写入train.txt
# ========================================================================
feature = read_data.read_feature('feature.txt')
word_set1, word_list1 = featureSelection.getClassDic('train10.txt')
word_set2, word_list2 = featureSelection.getClassDic('train50.txt')
idf_word_list, idf_count_list = read_data.read_idf('idf.txt')

N = len(word_list1) + len(word_list2)

write_data.write_weight('train_svm.txt', feature, word_list1, idf_count_list,10, N)
write_data.write_weight('train_svm.txt', feature, word_list2, idf_count_list,50, N)

# ========================================================================
# word_set = []
# word_set.append(word_set1)
# word_set.append(word_set2)
# word_list = []
# word_list.append(word_list1)
# word_list.append(word_list2)


# feature = featureSelection.selectFeature(word_set, word_list, 1000)
#
#
# # 将文本特征写入feature.txt文件
# fw = codecs.open('feature.txt','w','gbk')
# for f in feature:
#     fw.write(f)
#     fw.write('\n')
# fw.close()
