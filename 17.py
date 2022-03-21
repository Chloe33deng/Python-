a,b = eval(input("请输入两个整数,用逗号分隔:"))
if a > b:
    m,n = a,b
    while m%n != 0:
        m,n = n,m % n
    else:
        print("a和b的公约数是{}".format(n))
else:
    m,n = b,a
    while m % n != 0:
        m,n = n,m %n
    else:
        print("a和b的公约数是{}".format(n))
c = int(a * b / n)
print("a和b的最小公倍数是{}".format(c))
