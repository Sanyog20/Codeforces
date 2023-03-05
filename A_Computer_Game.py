for i in range(int(input())):
    n = int(input())
    row_1 = input()
    row_2 = input()
    ans = "YES"
    for j in range(n):
        if row_1[j] == '1' and row_2[j] == '1':
            ans = "NO"
            break
    print(ans)