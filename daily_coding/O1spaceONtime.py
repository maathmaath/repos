# a = [6, 1, 3, 3, 3, 6, 6]
# for i in reversed(range(len(a))):
#     x = a[i]
#     a.remove(x)
#     if x not in a:
#         print(x)
#         break
#     a.append(x)
#     print(a)

# prints no-repeting char in O(N) time and O(1) memory
a = [6, 1, 3, 3, 3, 6, 6]
for i in reversed(range(len(a))):
    x = a[i]
    del a[i]
    if x not in a:
        print(x)
        break
    a.append(x)
