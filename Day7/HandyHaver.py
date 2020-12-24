file = open("input.txt",'r')
tab = [n for n in file.readlines()]

tabSize = len(tab)

bags = [ rule.split("bags", 1)[0].strip() for rule in tab ]
matrix = [ [ False for i in range(tabSize + 1) ] for j in range(tabSize + 1) ]



for i in range(len(tab)):
    head = tab[i].split("bags", 1)[0].strip()
    opts = tab[i].split("bags", 1)[1].strip().replace("contain", "").replace("bags", "").replace("bag", "").split(",")

    if "no other" in opts[0]:
        matrix[i][tabSize] = True
        next
    else: 
        for opt in opts:
            param = opt.replace(".","").strip().split(" ", 1)
            matrix[i][bags.index(param[1])] = True


containShinyGold = []

for b in bags:
    stack = [b]
    while len(stack) > 0:
        name = stack.pop()
        if name in containShinyGold:
            containShinyGold.append(b)
            break

        index = bags.index(name)
        
        for i in range(len(matrix[index]) - 1):
            if matrix[index][i] and bags[i] == "shiny gold":
                containShinyGold.append(b)
                stack = []
            elif matrix[index][i]:
                stack.append(bags[i])




#print(matrix)
#print(bags)
#print(containShinyGold)
print(len(containShinyGold))
