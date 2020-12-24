import string

file = open("input.txt",'r')
tab = [n for n in file.read().split("\n\n")]

test = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
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
        else:
            content = tmp[i].split(':')[1]
            if t == test[0]:
                if int(content) > 2002 or int(content) < 1920:
                    validity = False
            elif t == test[1]:
                if int(content) > 2020 or int(content) < 2010:
                    validity = False
            elif t == test[2]:
                if int(content) > 2030 or int(content) < 2020:
                    validity = False
            elif t == test[3]:
                if "cm" in content:
                    value = int(content.strip("cm"))
                    if value < 150 or value > 193:
                        validity = False
                elif "in" in content:
                    value = int(content.strip("in"))
                    if value < 59 or value > 76:
                        validity = False
                else:
                    validity = False                    
            elif t == test[4]:
                if not(content[0] == "#" 
                        and len(content) == 7 
                        and all(c in string.hexdigits for c in content[1:])):
                    validity = False
            elif t == test[5]:
                if not(content == "amb" 
                        or content == "blu"
                        or content == "brn"
                        or content == "gry"
                        or content == "grn"
                        or content == "hzl"
                        or content == "oth"):
                    validity = False
            elif t == test[6]:
                if not(len(content) == 9 and content.isdigit()):
                    validity = False

    
    if validity:
        counter = counter + 1



print(counter)


