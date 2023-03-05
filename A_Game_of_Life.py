for i in range(int(input())):
    n, m = map(int, input().split())
    s = list(input())
    while m > 0:
        for j in range(n - 1):
            s1 = ['0' * n]
            if s[j] == '1':
                if j == 0:
                    if s[j + 1] == '0':
                        s1[j + 1] = '1'
                elif j == n - 1:
                    if s[j - 1] == '0':
                        s1[j - 1] = '1'
                else:
                    if s[j + 1] == '0':
                        s1[j + 1] = '1'
                        s1[j - 1] = '1'
                    else:
                        s1[j - 1] = '1'
            s = s1
            print(s1, s)
        m -= 1
    s1 = ""
    for j in s:
        s1 = s1 + j
    print(s1)