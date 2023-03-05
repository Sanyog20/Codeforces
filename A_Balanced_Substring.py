for i in range(int(input())):
    n = int(input())
    s = input()
    l = -1
    r = -1
    if n == 1:
        l = -1
        r = -1
    else:
        for j in range(n - 1):
            count_a = 0
            count_b = 0
            for k in range(j, n):
                if s[k] == 'a':
                    count_a = count_a + 1
                else:
                    count_b = count_b + 1
                if count_b == count_a:
                    l = j + 1
                    r = k + 1
                    break
            if count_a == count_b:
                break
    print(l, r)