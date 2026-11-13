class Solution(object):
    def sort(self, a):
        if len(a) <= 1:
            return a
        p = a[len(a) // 2]
        l = [x for x in a if x < p]
        m = [x for x in a if x == p]
        r = [x for x in a if x > p]
        return self.sort(l) + m + self.sort(r)

    def threeSum(self, a):
        a = self.sort(a)
        n = len(a)
        res = []
        for i in range(n - 2):
            if i > 0 and a[i] == a[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                s = a[i] + a[l] + a[r]
                if s == 0:
                    res.append(f"{a[i]} {a[l]} {a[r]}")
                    while l < r and a[l] == a[l + 1]:
                        l += 1
                    while l < r and a[r] == a[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return "\n".join(res) if res else "None"

n = int(input())
a = list(map(int, input().split()))
print(Solution().threeSum(a))
