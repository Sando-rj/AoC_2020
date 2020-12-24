file = open("input.txt",'r')
tab = [int(n) for n in file.readlines()]


diff = [0, 0, 1]
tab.append(0)
tab.sort()

for i in range(len(tab)-1):
    diff[tab[i+1] - tab[i] - 1] += 1

print(diff)
print(diff[0] * diff[2])
