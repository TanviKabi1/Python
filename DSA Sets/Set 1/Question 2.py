n = int(input())
a = list(map(int, input().split()))

seen = set()
res = -1
for x in a:
    if x in seen:
        res = x
        break
    seen.add(x)

print(res)
