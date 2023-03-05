for i in range(int(input())):
    n = int(input())
    s = input()
    s1 = ""
    for j in range(n):
        if s[j] == "U":
            s1 = s1 + "D"
        elif s[j] == "D":
            s1 = s1 + "U"
        else:
            s1 = s1 + s[j]
    print(s1)