class Solution(object):
    def sort(self, a):
        if len(a) <= 1:
            return a
        p = a[len(a) // 2]
        l = [x for x in a if x < p]
        m = [x for x in a if x == p]
        r = [x for x in a if x > p]
        return self.sort(l) + m + self.sort(r)

    def commonMembers(self, a, b):
        s = set(a)
        res = []
        seen = set()
        for x in b:
            if x in s and x not in seen:
                res.append(x)
                seen.add(x)
        if not res:
            return "None"
        res = self.sort(res)
        return " ".join(map(str, res))

m, n = map(int, input().split())
a = list(map(int, input().split())) if m > 0 else []
b = list(map(int, input().split())) if n > 0 else []
print(Solution().commonMembers(a, b))
