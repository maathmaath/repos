llist = []


def gen_word(llist):
    if llist:
        listb = []
        for j in llist:
            x = j
            for i in range(65, 91):
                x += chr(i)
                listb.append(x)
                x = j
        return listb
    else:
        for i in range(65, 91):
            llist.append(chr(i))
        return llist


password = "ravi"
l = len(password)

for i in range(l):
    llist = gen_word(llist)

with open("passwords.txt", 'w') as f:
    for i in llist:
        f.writelines(i+"\n")
