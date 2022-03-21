h  = [True] * 100
h[:2] = [False, False]
for i in range(2, int(100 ** 0.5) + 1):
    if h[i]:
        h[i*i::i] = [False] * len(h[i*i::i])

s=''
for i, e in enumerate(h):
    if e:
        s += str(i) + ' '
print(s.strip())
