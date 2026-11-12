n = int(input())
a = list(map(int, input().split()))

cnt = {}
for x in a:
    cnt[x] = cnt.get(x, 0) + 1

ans = -1
for x in a:
    if cnt[x] == 1:
        ans = x
        break

print(ans)
