def func1(a):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    for i in a:
        if i.isdigit():#数字
            count1+=1
        elif i.isalpha():#字母
            count2+=1
        elif i.isspace():#空格
            count3+=1
        else:#其他
            count4+=1
    print("数字有%d个：" % count1)
    print("字母有%d个：" % count2)
    print("空格有%d个：" % count3)
    print("其他有%d个：" % count4)
    return (count1, count2, count3, count4)
str_num = input("请输入任意字符串:")
func1(str_num)

