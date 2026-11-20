class Solution(object):
    def countSort(self, a):
        c = [0] * 101
        for x in a:
            c[x] += 1
        res = []
        for x in range(101):
            for _ in range(c[x]):
                res.append(x)
        return " ".join(map(str, res))

n = int(input())
a = list(map(int, input().split()))
print(Solution().countSort(a))
