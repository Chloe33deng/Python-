def repeat(txt):
    ls = eval(txt)
    counts = {}
    for i in ls:
        counts[i] = counts.get(i, 0) + 1
        if counts[i] > 1:
            return True
def main():
    txt = input('请输入一个列表：')
    print(repeat(txt))
main()
