import sys

input = sys.stdin.read
data = input().split()
if not data:
    exit()

n, q = int(data[0]), int(data[1])
idx = 2

pref = [0] * (n + 1)
for i in range(n):
    pref[i + 1] = pref[i] + int(data[idx])
    idx += 1

out = []
for _ in range(q):
    l = int(data[idx])
    r = int(data[idx + 1])
    idx += 2
    out.append(str(pref[r + 1] - pref[l]))

sys.stdout.write("\n".join(out) + "\n")
