class Solution(object):
    def inversions(self, a):
        def merge(arr):
            if len(arr) <= 1:
                return arr, 0
            mid = len(arr) // 2
            left, cl = merge(arr[:mid])
            right, cr = merge(arr[mid:])
            res = []
            i = j = 0
            count = cl + cr
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    count += len(left) - i
                    j += 1
            res.extend(left[i:])
            res.extend(right[j:])
            return res, count
        return merge(a)[1]

n = int(input())
a = list(map(int, input().split()))
print(Solution().inversions(a))
