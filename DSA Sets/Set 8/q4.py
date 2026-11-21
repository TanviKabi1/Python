class Solution(object):
    def searchRotated(self, a, t):
        l, r = 0, len(a) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if a[mid] == t:
                return mid
            if a[l] <= a[mid]:
                if a[l] <= t < a[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if a[mid] < t <= a[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

n = int(input())
a = list(map(int, input().split()))
t = int(input())
print(Solution().searchRotated(a, t))
