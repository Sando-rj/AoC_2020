from itertools import chain, combinations

file = open("input.txt",'r')
tab = [int(n) for n in file.readlines()]

def fact(n):
    output = 1
    for i in range(n):
        output *= i
    return output

def calculate_possible_set(set_num):
    pot_sets = chain.from_iterable(combinations(set_num[1:len(set_num)-1], r) for r in range(len(set_num)-1))
    counter = 0
    for s in pot_sets:
        s = (set_num[0],) + s + (set_num[-1],)
        i = 0
        while i < (len(s) - 1) and (s[i+1] - s[i]) <= 3 :
            i += 1
        if i == (len(s) - 1):
            counter += 1

    return counter
            

diff = [0, 0, 0]
tab.append(0)
tab.sort()
tab.append(tab[len(tab)-1] + 3)

count = 1
i = 0
while i < (len(tab) - 2):
    diff[tab[i+1] - tab[i] - 1] += 1
    if (tab[i+1] - tab[i]) > 1:
        i += 1
        next

    j = i
    while tab[j+1] - tab[j] < 3:
        j += 1

    possibilities = calculate_possible_set(tab[i:j+1])

    count *= possibilities
    i = j + 1


print(tab)
print("Answer : " + str(count))
