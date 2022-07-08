# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round F - Problem B. Festival
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887dba
#
# Time:  O(NlogN)
# Space: O(N)
#

# Template:
# https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/design-most-recently-used-queue.py
class BIT(object):  # 0-indexed.
    def __init__(self, n):
        self.__bit = [0]*(n+1)  # Extra one for dummy node.

    def add(self, i, val):
        i += 1  # Extra one for dummy node.
        while i < len(self.__bit):
            self.__bit[i] += val
            i += (i & -i)

    def query(self, i):
        i += 1  # Extra one for dummy node.
        ret = 0
        while i > 0:
            ret += self.__bit[i]
            i -= (i & -i)
        return ret

    def kth_element(self, k):
        floor_log2_n = (len(self.__bit)-1).bit_length()-1
        pow_i = 2**floor_log2_n
        total = pos = 0  # 1-indexed
        for _ in reversed(xrange(floor_log2_n+1)):  # O(logN)
            if pos+pow_i < len(self.__bit) and total+self.__bit[pos+pow_i] < k:  # find max pos s.t. total < k
                total += self.__bit[pos+pow_i]
                pos += pow_i
            pow_i >>= 1
        return (pos+1)-1  # 0-indexed, return min pos s.t. total >= k if pos exists else n

def festival():
    D, N, K = map(int, raw_input().strip().split())
    points, hs = [], []
    for i in xrange(N):
        h, s, e = map(int, raw_input().strip().split())
        points.append((s, 1, h, i))
        points.append((e+1, -1, h, i))
        hs.append((h, i))
    points.sort()
    hs.sort(reverse=True)

    idx_to_rank = {i:rank for rank, (_, i) in enumerate(hs)}
    bit1, bit2 = BIT(N), BIT(N)
    result = 0
    for _, c, h, i in points:
        if c == 1:
            bit1.add(idx_to_rank[i], h)
            bit2.add(idx_to_rank[i], 1)
            result = max(result, bit1.query(min(bit2.kth_element(K), N-1)))
        else:
            bit1.add(idx_to_rank[i], -h)
            bit2.add(idx_to_rank[i], -1)
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, festival())
