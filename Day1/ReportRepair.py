file = open("input.txt",'r')
tab = [int(n.strip()) for n in file.readlines()]

tab.sort()

i = 0
j = len(tab) - 1

while(tab[i] + tab[j] != 2020):
    if(tab[i] + tab[j] > 2020):
        j = j - 1
    else:
        i = i + 1

print(str(tab[i]) + " " + str(tab[j]))
print(tab[i] * tab[j])
