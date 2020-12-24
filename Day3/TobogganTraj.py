file = open("input.txt",'r')
tab = [n.strip() for n in file.readlines()]

x = 0
y = 0
tree = 0

while y < len(tab) - 1:
    x = (x + 3) % (len(tab[0]))
    y = y + 1

    if(tab[y][x] == '#'):
        tree = tree + 1

print(tree)
