file = open("input.txt",'r')
tab = [int(n.strip()) for n in file.readlines()]

tab.sort()

i = 0
j = len(tab) - 1
k = 0

while(tab[i] + tab[j] + tab[k] != 2020):
    if(tab[i] + tab[j] + tab[k] > 2020):
        j = j - 1
    elif(tab[j] - tab[i] > tab[k]):
        k = k + 1
    else:
        i = i + 1
        k = 0
        

print(str(tab[i]) + " " + str(tab[j]) + " " + str(tab[k]))
print(tab[i] * tab[j] * tab[k])
