for _ in range(int(input())):
    s = input()
    if s.count('2') == 0 and s.count('4') == 0 and s.count('6') == 0 and s.count('8') == 0:
        ans = -1
    elif s[-1] == '2' or s[-1] == '4' or s[-1] == '6' or s[-1] == '8':
        ans = 0
    elif s[0] == '2' or s[0] == '4' or s[0] == '6' or s[0] == '8':
        ans = 1
    else:
        ans = 2
    print(ans)
