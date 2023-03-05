n = int(input())
lib = []
count = 0
max_count = 0
for i in range(n):
    s = input()
    if s[0] == '+':
        lib.append(s[2:])
        count += 1
        if count > max_count:
            max_count = count
    else:
        if s[2:] in lib:
            count -= 1
            lib.remove(s[2:])
        else:
            max_count += 1
print(max_count)
