class Solution(object):
    def insertSort(self, a):
        n = len(a)
        shifts = 0
        for i in range(1, n):
            cur = a[i]
            j = i - 1
            while j >= 0 and a[j] > cur:
                a[j + 1] = a[j]
                shifts += 1
                j -= 1
            a[j + 1] = cur
        return " ".join(map(str, a)) + "\n" + str(shifts)
n = int(input())
a = list(map(int, input().split()))
print(Solution().insertSort(a))
