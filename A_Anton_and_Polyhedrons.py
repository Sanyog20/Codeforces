n = int(input())
s = []
for i in range(n):
    s1 = input()
    s.append(s1)
t1 = s.count("Tetrahedron") * 4
t2 = s.count("Cube") * 6
t3 = s.count("Octahedron") * 8
t4 = s.count("Dodecahedron") * 12
t5 = s.count("Icosahedron") * 20
print(t1 + t2 + t3 + t4 + t5)
