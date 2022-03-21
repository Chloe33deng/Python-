n = input("输入一行字符:")
num = chi = eng1 = eng2 = other = 0
a = n.count(" ")
print("空格的个数是{}".format(a))
for i in n:
    if 19968 <= ord(i) <= 40869:
        chi += 1
    elif 48 <= ord(i) <= 57:
        num += 1
    elif 97 <= ord(i) <= 122:
        eng1 += 1
    elif 65 <= ord(i) <= 90:
        eng2 += 1
    else:
        total = chi + num + eng1 + eng2
        other = int(len(n) - total)
print("汉字的个数是{}".format(chi))
print("数字的个数是{}".format(num))
print("小写字母的个数是{}".format(eng1))
print("大写字母的个数是{}".format(eng2))
print("其他字母的个数是{}".format(other))
