# author:lin huiqing
# date: 12:14 Monday 22/10/2018

import csv

#----------------------STEP1 and STEP2----------------------#
## use a list to store the relative files
lists = [   'txt/trade-wars-news1.txt', 'txt/trade-wars-news2.txt', 
            'txt/trade-wars-news3.txt', 'txt/trade-wars-news4.txt', 'txt/trade-wars-news5.txt']

## read all txt.files and split them
files = []
for i in lists:
    with open(i, 'r')as article:
        files.extend(article.read().split())

#----------------------------STEP3--------------------------#
## count word frequency

# method1

# 假如使用append输出值为5（element个数），extend输出值为所有单词个数  tip：需要区分append与extend

# lens = len(files[0]) + len(files[1]) + len(files[2]) + len(files[3]) + len(files[4]) 
# print(lens)

# lens = 0
# for i in range(5):
#     lens = lens + len(files[i])
# print(lens) 

# for j in range(len(files)):
#     for i in files:
#     if i == files[j]:
#         counter = counter + 1

# method2

# 输出的结果是list中含有多个dict，不易于之后的操作，complicated
# words = []
# for i in range(len(files)):
#     word = {files[i] : files.count(files[i])}
#     words.append(word)

# method3
# 输出的结果是一个dict， syntax： dict[key] = value
words = {}
for word in files :
    words[word] = files.count(word)

#----------------------------Bonus--------------------------#

stopwords = []
with open('stopwords.txt','r') as fp:
    stopwords.extend(fp.read().split())
 
# stop_words = ["the","and","of","a","in"]
# for k in stop_words:
#     words.pop(k)

for k in stopwords:
    if k in words.keys():
        words.pop(k)


#----------------------------STEP4--------------------------#
## rank

# methond1:输出是一个list
# rank_of_frequency = sorted(words.items(),key = lambda item:item[1], reverse = True)

# methond2-wrong
# def sort_by_value(words):
#     items = words.items()
#     new_items = []
#     for v in items:
#         new_items.append((v[1], v[0]))
#     new_items.sort(reverse = True )
#     key_items = []
#     for i in range(0,len(new_items)):
#         key_items.append(new_items[i][1])
#     return key_items

# methond3:输出是一个dict
def sort_freq(dict):
    rank_of_frequency = {}
    b = dict.items()
    a = sorted(dict.values(), reverse = True )
    for i in range(len(a)):    
    # a[0]
        for item in b:
            if a[i] == item[1]:
                rank_of_frequency[item[0]] = a[i]
    return rank_of_frequency

rank_of_frequency =  sort_freq(words)


## output the first 15 keywords freqquency

# method1:(compilicated)
# top_15_keywords = []
# for i in range(15):
#     top_15_keywords.append(rank_of_frequency[i])
# print(top_15_keywords)

# method2:(easy)
# list_rof = []
# list_rof = list(rank_of_frequency.items())
# for i in range(15):
#     # print(list(rank_of_frequency.items())[i])
#     print(list_rof[i])

# method3:(easy)
for item in list(rank_of_frequency.items())[:15]:
    print(item)

# #----------------------------STEP5--------------------------#
# ## csv

with open('keyword_frequency_list.csv','w') as f:
    mywriter = csv.writer(f)
    mywriter.writerow(['keyword','frequency'])
    # mywriter.writerows(rank_of_frequency)

    for key, value in rank_of_frequency.items():
        mywriter.writerow([key, value])

