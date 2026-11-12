n = int(input())
a = list(map(int, input().split()))

tot = 0
for x in a:
    tot += x

left = 0
ans = -1
for i in range(n):
    if left == tot - left - a[i]:
        ans = i
        break
    left += a[i]

print(ans)
