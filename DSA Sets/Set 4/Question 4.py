class Solution(object):
    def findAnagrams(self, s, p):
        if len(s) < len(p):
            return "None"
        cp = [0] * 26
        cs = [0] * 26
        for ch in p:
            cp[ord(ch) - 97] += 1
        k = len(p)
        for i in range(k):
            cs[ord(s[i]) - 97] += 1
        res = []
        if cs == cp:
            res.append(0)
        for i in range(k, len(s)):
            cs[ord(s[i]) - 97] += 1
            cs[ord(s[i - k]) - 97] -= 1
            if cs == cp:
                res.append(i - k + 1)
        return " ".join(map(str, res)) if res else "None"

s = input().strip()
p = input().strip()
print(Solution().findAnagrams(s, p))
