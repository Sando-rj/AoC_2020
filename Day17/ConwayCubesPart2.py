import copy
from itertools import product

file_name = open("input.txt", 'r')

start = [ line.strip() for line in file_name.readlines() ]

#start = [".#.",
#         "..#",
#         "###"]
cycle_num = 6
#cycle_num = 2 

cycle_num = cycle_num + 1

#Print Output
def display_cube(hypercube):
    print(str(len(hypercube)) + " " + str(len(hypercube[0])) + " " + str(len(hypercube[0][0])) + " " + str(len(hypercube[0][0][0])))
    for k in range(1, len(hypercube) - 1):
        print('<'*10 + " w=" + str(k-cycle_num))
        for j in range(1, len(hypercube[k]) - 1):
            print('-'*10 + " z=" + str(j-cycle_num))
            for i in range(1, len(hypercube[k][j]) - 1):
                print( hypercube[k][j][i][1:len(hypercube[k][j][i]) - 1] )


def count_activated(hypercube):
    count = 0
    for cube in hypercube:
        for plane in cube:
            for line in plane:
                for pixel in line:
                    if pixel == '#':
                        count += 1
    return count

#Create Conway Cube Space
blank_lines = "." * ( cycle_num * 2 + len(start[0]) )
blank_canvas = [ copy.deepcopy(blank_lines) for i in range(len(start) + cycle_num * 2) ]
blank_space = [ copy.deepcopy(blank_canvas) for i in range(cycle_num * 2 + 1) ]
work_canvas = [ copy.deepcopy(blank_lines) if ((i - cycle_num) < 0 or (i - cycle_num) >= len(start)) 
        else ( "." * cycle_num + start[i - cycle_num] + "." * cycle_num) 
        for i in range(len(start) + cycle_num * 2) ]
work_space = [ copy.deepcopy(work_canvas) if ( i - cycle_num ) == 0 else copy.deepcopy(blank_canvas) for i in range(cycle_num * 2 + 1) ]
work_hyperspace = [ copy.deepcopy(work_space) if ( i - cycle_num ) == 0 else copy.deepcopy(blank_space) for i in range(cycle_num * 2 + 1) ]

neighbours_pos = list(product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1], [-1, 0, 1]))
neighbours_pos.remove((0,0,0,0))

#Live cycles
for c in range(cycle_num - 1):
    x = 0
    y = 0
    z = 0
    w = 0
    comparison_hyperspace = copy.deepcopy(work_hyperspace)
#    display_cube(comparison_hyperspace)
#    display_cube(work_hyperspace)
#    print('>'*30)
    for w in range(1, len(comparison_hyperspace) - 1):
        for z in range(1, len(comparison_hyperspace[0]) - 1):
            for y in range(1, len(comparison_hyperspace[0][0]) - 1):
#               print(work_hyperspace[w][z][y])
                newline = comparison_hyperspace[w][z][y]
                for x in range(1, len(comparison_hyperspace[0][0][0]) - 1):
                    neighbourhood = sum([ 1 if comparison_hyperspace[w+n[0]][z+n[1]][y+n[2]][x+n[3]] == '#' else 0 for n in neighbours_pos])
                    if(comparison_hyperspace[w][z][y][x] == '#' and not(neighbourhood == 2 or neighbourhood == 3)):
#                       print("# -> .")
#                       print("Before change : " + work_hyperspace[w][z][y])
                        newline = newline[:x] + '.' + newline[x+1:]
#                       print("After  change : " + work_hyperspace[w][z][y])
	
                    if(comparison_hyperspace[w][z][y][x] == '.' and neighbourhood == 3):
#                       print(". -> #")
#                       print("Before change : " + work_hyperspace[w][z][y])
                        newline = newline[:x] + '#' + newline[x+1:]
#                       print("After  change : " + work_hyperspace[w][z][y])
	
#                    print(" x : " + str(x) + " y : " + str(y) + " z : " + str(z) + " w : " + str(w) + " sum : " + str(neighbourhood) + " " + comparison_hyperspace[w][z][y][x] + " -> " + work_hyperspace[w][z][y][x])
                work_hyperspace[w][z][y] = newline
#               print(work_hyperspace[w][z][y])
#    print('#' * 20 + " " + str(c+1) + " " + '#' * 20)
#    display_cube(work_hyperspace)    
#    print('<'*30)

print(count_activated(work_hyperspace))
