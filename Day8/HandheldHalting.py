file = open("input.txt",'r')
tab = [n.strip().split(' ') for n in file.readlines()]
visited = [ False for i in range(len(tab)) ]

acc = 0

#Part 1 answer, just add the accumulator and count then return
def doesItEnd():
    i = 0
    visited = [ False for i in range(len(tab)) ]
    while i < len(tab) and not(visited[i]):
        visited[i] = True
        if tab[i][0] == "jmp":
            i = i + int(tab[i][1])
        else:
            i = i + 1
    return i == len(tab)


for t in range(len(tab)):
    if tab[t][0] == "nop":
        tab[t][0] = "jmp"
        if not(doesItEnd()):
            tab[t][0] = "nop"
        else:
            break

    elif tab[t][0] == "jmp":
        tab[t][0] = "nop"
        if not(doesItEnd()):
            tab[t][0] = "jmp"
        else:
            break

i = 0
while i < len(tab) and not(visited[i]):
    visited[i] = True
    if tab[i][0] == "acc":
        acc = acc + int(tab[i][1])
        i = i + 1
    elif tab[i][0] == "jmp":
        i = i + int(tab[i][1])
    else:
        i = i + 1

print("Falty line : ")
print(tab[t])
print(str(t) + " " + str(acc))
