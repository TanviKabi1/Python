class Solution(object):
    def sortIntervals(self, a):
        if len(a) <= 1:
            return a
        p = a[len(a) // 2]
        l = [x for x in a if x[0] < p[0] or (x[0] == p[0] and x[1] < p[1])]
        m = [x for x in a if x == p]
        r = [x for x in a if x[0] > p[0] or (x[0] == p[0] and x[1] > p[1])]
        return self.sortIntervals(l) + m + self.sortIntervals(r)

    def mergeIntervals(self, a):
        a = self.sortIntervals(a)
        res = []
        cur = list(a[0])
        for i in range(1, len(a)):
            if a[i][0] <= cur[1]:
                if a[i][1] > cur[1]:
                    cur[1] = a[i][1]
            else:
                res.append(f"{cur[0]} {cur[1]}")
                cur = list(a[i])
        res.append(f"{cur[0]} {cur[1]}")
        return "\n".join(res)

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
print(Solution().mergeIntervals(a))
