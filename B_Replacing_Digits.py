n = list(input())
s = list(input())
s.sort()
s = s[::-1]
for i in range(len(n)):
    if s[0] > n[i] and len(s) != 0:
        n[i] = s[0]
        s.remove(s[0])
ans = ""
for i in range(len(n)):
    ans = ans + n[i]
print(ans)
