from itertools import permutations
s = input()
s1 = list(permutations(s))
for i in s1:
    s2 = ""
    for j in i:
        s2 = s2 + j
    print(s2, end=" ")
print()
print(s1)
