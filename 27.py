txt = input("请输入一段中文文本：")
counts = {}
for i in txt:
    counts[i] = counts.get(i, 0) + 1
ls = list(counts.items())
ls.sort(key=lambda x:x[1], reverse=True)
#指定列表中那一列作为排序的列
for i in range(len(counts)):
    word, count = ls[i]
    print ("{0:<10}{1:>5}".format(word, count))
