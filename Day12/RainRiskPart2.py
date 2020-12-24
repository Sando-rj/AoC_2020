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

w_x = 10
w_y = 1

i = 0
for d in tab:
    print(d)

    if d[0] == 'N':
        w_y += d[1] 
    elif d[0] == 'S':
        w_y -= d[1]
    elif d[0] == 'E':
        w_x += d[1]
    elif d[0] == 'W':
        w_x -= d[1]

    elif d[0] == 'L':
        dInRad = math.radians(d[1])
        w_x, w_y = [ (w_x - x) * math.cos(dInRad) - (w_y - y) * math.sin(dInRad) + x, 
                (w_x - x) * math.sin(dInRad) + (w_y - y) * math.cos(dInRad) + y]
    elif d[0] == 'R':
        dInRad = math.radians(d[1])
        w_x, w_y = [ (w_x - x) * math.cos(-dInRad) - (w_y - y) * math.sin(-dInRad) + x, 
                (w_x - x) * math.sin(-dInRad) + (w_y - y) * math.cos(-dInRad) + y]
    elif d[0] == 'F':
        dx = w_x - x
        dy = w_y - y

        x += dx * d[1]
        w_x += dx * d[1]
        y += dy * d[1]
        w_y += dy * d[1]
    
    print(" waypoint : x " + str(w_x) + " y " + str(w_y)) 
    print(" boat : x " + str(x) + " y " + str(y)) 

print("Result : " + str(x) + " " + str(y) + " Manhattan " + str((abs(x) + abs(y))))
