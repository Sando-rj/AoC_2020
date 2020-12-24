file = open("input.txt",'r')
tab = [int(n) for n in file.readlines()]

preamble = 25

i = 0
error = 0

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
        error = tab[i]
        break

if error != 0:
    for i in range(len(tab)):
        acc = 0
        j = i
        while j < len(tab) and acc < error:
            acc = acc + tab[j]
            j = j + 1
        if acc == error:
            answer = tab[i:j]
            answer.sort()
            print("Ids from " + str(i) + " to " + str(j) + " Values sums to : " + str(answer[0] + answer[len(answer) -1]))
            break

print("End")
