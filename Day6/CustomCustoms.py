file = open("input.txt",'r')
tab = [n.split('\n') for n in file.read().split("\n\n")]

resP1 = 0
resP2 = 0

for g in tab:
    r = set("")
    s = set("abcdefghijklmnopqrstuvwxyz")
    
    for e in g:
        if e != '':
            r = r.union(set(e))
            s = s.intersection(set(e))
    
    resP1 = resP1 + len(r)
    resP2 = resP2 + len(s)

print("Part 1 count : " + str(resP1))
print("Part 2 count : " + str(resP2))
