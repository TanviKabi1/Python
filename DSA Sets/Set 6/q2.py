class Solution(object):
    def sortColors(self, a):
        l, m, r = 0, 0, len(a) - 1
        while m <= r:
            if a[m] == 0:
                a[l], a[m] = a[m], a[l]
                l += 1
                m += 1
            elif a[m] == 1:
                m += 1
            else:
                a[m], a[r] = a[r], a[m]
                r -= 1
        return " ".join(map(str, a))

n = int(input())
a = list(map(int, input().split()))
print(Solution().sortColors(a))
