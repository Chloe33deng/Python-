def isNum(i):
    try:
        i = type(eval(i))
        if i == type(123):
            return True
        elif i == type(12.3):
            return True
        elif i == type(12 + 3j):
            return Ture
    except :
        return False
i = input("请输入一个字符串:")
print(isNum(i))
