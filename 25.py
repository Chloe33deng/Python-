def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib(n - 1) + fib(n - 2)
 
def main():
    n = eval(input("请输入一个整数："))
    print(fib(n))
 
main()

