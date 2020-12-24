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


verif = False
it = 0
while not(verif):
    it += 1
    verif_tab = original_tab.copy()
    verif = True
    for y in range(len(verif_tab)):
        for x in range(len(verif_tab[0])):
            if verif_tab[y][x] == '.':
               continue 

            sum = 0
            alldir = 0
            fact = 1
            test = [ [False, False, False], [False, True, False], [False, False, False] ]
            while alldir < 8:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if not(test[i+1][j+1]) and ((y + i * fact) < 0 or (y + i * fact) > (len(verif_tab) - 1) or (x + j * fact) < 0 or (x + j * fact) > (len(verif_tab[0]) - 1)):
                            test[i + 1][j + 1] = True
                            alldir += 1
                            continue

                        if not(test[i+1][j+1]) and (i != 0 or j != 0) and (verif_tab[y + i * fact][x + j * fact] == '#'):
                            sum += 1
                            test[i + 1][j + 1] = True
                            alldir += 1
                            continue
                        
                        if not(test[i+1][j+1]) and (i != 0 or j != 0) and (verif_tab[y + i * fact][x + j * fact] == 'L'):
                            test[i + 1][j + 1] = True
                            alldir += 1
                            continue
                fact += 1

            if sum == 0:
                original_tab[y] = original_tab[y][:x] + '#' + original_tab[y][x+1:]
            elif sum >= 5:
                original_tab[y] = original_tab[y][:x] + 'L' + original_tab[y][x+1:]
            
            if original_tab[y][x] != verif_tab[y][x]:
                verif = False

counter = 0
for y in original_tab:
    for x in y:
        if x == '#':
            counter += 1 

print("End at iteration : " + str(it))
print("Answer : " + str(counter))


