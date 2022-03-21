def save_csv(ls, fname):
    # 向列表中逐个添加元素
    value = input('请向列表总添加一个元素：')
    while value != '':
        ls.append(value)
        value = input('请向列表总添加一个元素：')
    print('您输入的列表为：{}'.format(ls))
    
    # 若元素中有半角逗号，将其替换成点
    for i in range(len(ls)):
        if ',' in ls[i]:
            ls[i] = ls[i].replace(',', '.')

    file_csv = open('{}.csv'.format(fname), 'w', encoding='utf-8')
    file_csv.write(','.join(ls) + '\n')
    file_csv.close()
    print('恭喜！已成功保存<{}.csv>文件！'.format(fname))


def read_csv(lt, fname):
    f = open('{}.csv'.format(fname), 'r', encoding='utf-8')
    lt = f.read().strip('\n').split(',')
    
    # 将替换后的点换成半角逗号
    for i in range(len(lt)):
        if '.' in lt[i]:
            lt[i] = lt[i].replace('.', ',')
    f.close()
    print('<{}.csv>文件读取中...'.format(fname))
    print(lt)


def main():
    ls = []
    fname = input('请将列表文件命名：')
    save_csv(ls, fname)
    lt = []
    read_csv(lt,fname)

main()
