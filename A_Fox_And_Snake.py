n, m = map(int, input().split())
s1 = "#" * m
s4 = "#" + ("." * (m - 1))
s3 = s1
s2 = ("." * (m - 1)) + "#"
t = [s1, s2, s3, s4]
for i in range(n):
    print(t[i % 4])