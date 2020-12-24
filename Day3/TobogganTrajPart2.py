file = open("input.txt",'r')
tab = [n.strip() for n in file.readlines()]

parameters = [ (1, 1), (3, 1), (5, 1), (7, 1), (1, 2) ]

x = 0
y = 0
tree = 0
res = 1

for p in parameters:
    tree = 0
    x = 0
    y = 0
    print(str(p[0]) + " " + str(p[1]))
    while y < len(tab) - 1:
        x = (x + p[0]) % (len(tab[0]))
        y = y + p[1]

        if(tab[y][x] == '#'):
            tree = tree + 1
    print(tree)
    res = res * tree

print(res)
