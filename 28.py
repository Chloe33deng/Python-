import random
txt = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ls = list(txt)
for i in range(10):
    a = ""
    for i in range(8):
        a = random.choice(ls) + a
    print(a)
