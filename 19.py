while True:
    try:
        n = int(input("请输入一个年份:"))
        if n % 4 == 0 & n % 100 != 0:
            print("{}年是闰年".format(n))
        elif n % 400 == 0:
            print("{}年是闰年".format(n))
        else:
            print("{}年是平年".format(n))
    except:
        print("输入内容必须为整数!")
        continue

