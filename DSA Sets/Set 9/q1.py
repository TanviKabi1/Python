class Solution(object):
    def budgetPairing(self, a, t):
        l, r = 0, len(a) - 1
        while l < r:
            s = a[l] + a[r]
            if s == t:
                return f"{l + 1} {r + 1}"
            elif s < t:
                l += 1
            else:
                r -= 1

n = int(input())
a = list(map(int, input().split()))
t = int(input())
print(Solution().budgetPairing(a, t))
