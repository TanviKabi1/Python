s = input()

filtered = []
for ch in s:
    if ch.isalnum():
        filtered.append(ch.lower())

i, j = 0, len(filtered) - 1
is_pal = True
while i < j:
    if filtered[i] != filtered[j]:
        is_pal = False
        break
    i += 1
    j -= 1

print("YES" if is_pal else "NO")
