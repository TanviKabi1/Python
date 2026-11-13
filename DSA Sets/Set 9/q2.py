class Solution(object):
    def trimmedMean(self, a, t):
        cnt = [0] * 101
        for x in a:
            cnt[x] += 1
        rem_low = t
        for v in range(101):
            if cnt[v] >= rem_low:
                cnt[v] -= rem_low
                break
            else:
                rem_low -= cnt[v]
                cnt[v] = 0
        rem_high = t
        for v in range(100, -1, -1):
            if cnt[v] >= rem_high:
                cnt[v] -= rem_high
                break
            else:
                rem_high -= cnt[v]
                cnt[v] = 0
        tot = 0
        c = 0
        for v in range(101):
            tot += v * cnt[v]
            c += cnt[v]
        return f"{tot / c:.2f}"

n, t = map(int, input().split())
a = list(map(int, input().split()))
print(Solution().trimmedMean(a, t))
