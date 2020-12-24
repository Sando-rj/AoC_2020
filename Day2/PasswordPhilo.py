file = open("input.txt",'r')
tab = [(n.split(' ')[0], n.split(' ')[1].strip(':'), n.split(' ')[2].strip()) for n in file.readlines()]

valid = 0

for v in tab:
    counter = 0
    for c in v[2]:
        if c == v[1]:
            counter = counter + 1
    if counter >= int(v[0].split('-')[0]) and counter <= int(v[0].split('-')[1]):
        valid = valid + 1

print(str(valid) + " " + str(len(tab)))

