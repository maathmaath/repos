f, s = 0, 1
for i in range(10):
    s += f
    f = s-f
    print(s)
