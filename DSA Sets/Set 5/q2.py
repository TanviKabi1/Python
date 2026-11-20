class Solution(object):
    def selectK(self, a, k):
        n = len(a)
        for i in range(k):
            m = i
            for j in range(i + 1, n):
                if a[j] < a[m]:
                    m = j
            a[i], a[m] = a[m], a[i]
        return " ".join(map(str, a[:k]))

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(Solution().selectK(a, k))
