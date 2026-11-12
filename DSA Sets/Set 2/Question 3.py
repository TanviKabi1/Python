n, t = map(int, input().split())
a = list(map(int, input().split()))

cur, best = 0, 0
for x in a:
    if x >= t:
        cur += 1
        if cur > best:
            best = cur
    else:
        cur = 0

print(best)
