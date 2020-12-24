file = open("input.txt",'r')
tab = [n for n in file.read().split("\n\n")]

test = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] #, "cid"]

counter = 0

for p in tab:
    validity = True
    tmp = []
    for v in p.strip().split(' '):
        for v2 in v.split('\n'):
            tmp.append(v2)
    for t in test:
        i = 0
        while i < len(tmp) and tmp[i].split(':')[0] != t:
            i = i + 1
        if i == len(tmp):
            validity = False
    if validity:
        counter = counter + 1

print(counter)


