class Solution(object):
    def bubble(self, a):
        n = len(a)
        passes = 0
        for i in range(n):
            swapped = False
            for j in range(n - 1 - i):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    swapped = True
            if swapped:
                passes += 1
            else:
                break
        return " ".join(map(str, a)) + "\n" + str(passes)

n = int(input())
a = list(map(int, input().split()))
print(Solution().bubble(a))
