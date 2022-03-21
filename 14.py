s = input('请输入一个6位数的自然数:\n')
l = s[::-1]
while s==l:
    print('您输入的是回文数！')
    break
else:
    print('您输入的不是回文数!')
