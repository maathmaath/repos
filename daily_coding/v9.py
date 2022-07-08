def check(m, n, no, p):
    least_lis = []
    for i in range(no):
        # bin_i = bin(i)[2:]
        bn = "0:0{}b".format(p)
        binx = "{"+bn+"}"
        bin_i = binx.format(i)
        if bin_i == m[0]:
            pass
        else:
            least_lis.append(0)
            for k in n:
                for l in range(p):
                    if int(bin_i[l]) ^ int(k[l]) == 1:
                        least_lis[len(least_lis)-1] += 1
    # return min(zip(least_lis.values(), least_lis.keys()))
    return min(least_lis)


def solution():
    t = int(input())
    for k in range(t):
        n, m, p = map(int, input().split(' '))
        max_no = p**2
        choose_lis = []
        forb_lis = []
        for i in range(n):
            bin_str = str(input())
            choose_lis.append(bin_str)
        for i in range(m):
            bin_str = str(input())
            forb_lis.append(bin_str)
        print(f"Case #{k+1}: {check(forb_lis,choose_lis, max_no, p)}")


solution()
