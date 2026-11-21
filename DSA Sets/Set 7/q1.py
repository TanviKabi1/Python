class Solution(object):
    def findID(self, a, q):
        l, r = 0, len(a) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if a[mid] == q:
                return mid
            elif a[mid] < q:
                l = mid + 1
            else:
                r = mid - 1
        return -1

n = int(input())
a = list(map(int, input().split()))
q = int(input())
print(Solution().findID(a, q))
