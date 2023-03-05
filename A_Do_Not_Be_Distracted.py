for _ in range(int(input())):
    n = int(input())
    s = input()
    flag = 1
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            t = s.rfind(s[i])
            if t != i:
                flag = 0
                break
    if flag:
        print("YES")
    else:
        print("NO")