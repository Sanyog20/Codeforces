for _ in range(int(input())):
    s = input()
    count = 0
    s1 = s[:2]
    for i in range(2, len(s) - 1, 2):
        s1 = s1 + s[i + 1]
    print(s1)
