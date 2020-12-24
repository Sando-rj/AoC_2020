import math

file = open("input.txt",'r')
tab = [(n.strip()[0], int(n.strip()[1:])) for n in file.readlines()]

#tab = [("F",10),
#("N", 3),
#("F", 7),
#("R", 90),
#("F", 11)]

x = 0
y = 0

facing = [ 1, 0] 
i = 0
for d in tab:
    if d[0] == 'N':
        y += d[1] 
    elif d[0] == 'S':
        y -= d[1]
    elif d[0] == 'E':
        x += d[1]
    elif d[0] == 'W':
        x -= d[1]

    elif d[0] == 'L':
        dInRad = math.radians(d[1])
        facing = [ facing[0] * math.cos(dInRad) - facing[1] * math.sin(dInRad), 
                facing[0] * math.sin(dInRad) + facing[1] * math.cos(dInRad) ]
    elif d[0] == 'R':
        dInRad = math.radians(d[1])
        facing = [ facing[0] * math.cos(-dInRad) - facing[1] * math.sin(-dInRad), 
                facing[0] * math.sin(-dInRad) + facing[1] * math.cos(-dInRad) ]
    elif d[0] == 'F':
        x += facing[0] * d[1]
        y += facing[1] * d[1]

    facing = [ int(facing[0]), int(facing[1]) ]

print(facing)
print("Result : " + str(x) + " " + str(y) + " Manhattan " + str((abs(x) + abs(y))))
