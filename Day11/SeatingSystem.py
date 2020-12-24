file = open("input.txt",'r')
original_tab = [n.strip() for n in file.readlines()]

#original_tab = [ "L.LL.LL.LL",
#"LLLLLLL.LL",
#"L.L.L..L..",
#"LLLL.LL.LL",
#"L.LL.LL.LL",
#"L.LLLLL.LL",
#"..L.L.....",
#"LLLLLLLLLL",
#"L.LLLLLL.L",
#"L.LLLLL.LL" ]


wall = '.' * len(original_tab[0])
original_tab.insert(0, wall)
original_tab.append(wall)

for i in range(len(original_tab)):
    original_tab[i] = '.' + original_tab[i] + '.'

verif = False
while not(verif):
    verif_tab = original_tab.copy()
    verif = True
    for y in range(1, len(verif_tab) - 1):
        for x in range(1, len(verif_tab[0]) - 1):
            if verif_tab[y][x] == '.':
               continue 

            sum = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if ((i != 0 or j != 0) and (verif_tab[y + i][x + j] == '#')):
                        sum += 1
            if sum == 0:
                original_tab[y] = original_tab[y][:x] + '#' + original_tab[y][x+1:]
            elif sum >= 4:
                original_tab[y] = original_tab[y][:x] + 'L' + original_tab[y][x+1:]
            
            if original_tab[y][x] != verif_tab[y][x]:
                verif = False

counter = 0
for y in original_tab:
    for x in y:
        if x == '#':
            counter += 1 

print(counter)


