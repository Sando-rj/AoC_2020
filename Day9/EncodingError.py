file = open("input.txt",'r')
tab = [int(n) for n in file.readlines()]

preamble = 25

for i in range(preamble,len(tab)):
    tmp = tab[i - preamble:i]
    tmp.sort()
    j = 0
    k = len(tmp) - 1
    while j != k and tmp[j] + tmp[k] != tab[i]:
        if tmp[j] + tmp[k] < tab[i]:
            j = j + 1
        else:
            k = k - 1
    if j == k:
        print(" Id : " str(i) + " Value : " + str(tab[i]))
        break

print("End")
