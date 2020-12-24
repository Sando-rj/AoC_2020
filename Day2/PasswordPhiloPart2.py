file = open("input.txt",'r')
tab = [(n.split(' ')[0], n.split(' ')[1].strip(':'), n.split(' ')[2].strip()) for n in file.readlines()]

valid = 0

for v in tab:
    pos1 = int(v[0].split('-')[0]) - 1
    pos2 = int(v[0].split('-')[1]) - 1

    if (v[2][pos1] == v[1] or v[2][pos2] == v[1]) and not( v[2][pos1] == v[1] and v[2][pos2] == v[1]):
        valid = valid + 1
    
    

print(str(valid) + " " + str(len(tab)))

