n = eval(input("请输入一个年份:"))
if n % 4 == 0 & 100 != 0:
    print("{}年是闰年".format(n))
elif n % 400 == 0:
    print("{}年是闰年".format(n))
else:
    print("{}年是平年".format(n))
