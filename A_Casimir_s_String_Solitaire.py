for i in range(int(input())):
    s = input()
    a_count = s.count('A')
    b_count = s.count('B')
    c_count = s.count('C')
    if a_count + c_count == b_count:
        print("YES")
    else:
        print("NO")