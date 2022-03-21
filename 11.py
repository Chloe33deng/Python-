while True:
    n = int(input("请输入一个整数:"))
    if n < 100:
        print('输入的整数不足三位数')
    else:
        print('该整数百位及以上数字:',n // 100)
        break
