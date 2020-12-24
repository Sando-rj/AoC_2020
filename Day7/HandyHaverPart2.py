# Not solved yet

file = open("input.txt",'r')
tab = [n for n in file.readlines()]

tabSize = len(tab)

bags = [ rule.split("bags", 1)[0].strip() for rule in tab ]
matrix = [ [ 0 for i in range(tabSize + 1) ] for j in range(tabSize + 1) ]



for i in range(len(tab)):
    head = tab[i].split("bags", 1)[0].strip()
    opts = tab[i].split("bags", 1)[1].strip().replace("contain", "").replace("bags", "").replace("bag", "").split(",")

    if "no other" in opts[0]:
        matrix[i][tabSize] = -1
        next
    else: 
        for opt in opts:
            param = opt.replace(".","").strip().split(" ", 1)
            matrix[i][bags.index(param[1])] = param[0]





stack = ["shiny gold"]
visited = []
nmbInVisited = []
count = 0


def recCalcBag(index, count):
    name = bags[index]
    count = count + 1

    for i in range(len(matrix[index]) -1):
        if int(matrix[index][i]) > 0:
            cout = count + int(matrix[index][i]) * recCalcBag(i, count)

    if i == tabSize:
        return 1

    return count


    
name = stack.pop()
index = bags.index(name)
counter = recCalcBag(index, 0) 
print(counter)         



#print(matrix)
#print(bags)
