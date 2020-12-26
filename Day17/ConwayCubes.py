import copy
from itertools import product

file_name = open("input.txt", 'r')

start = [ line.strip() for line in file_name.readlines() ]

#start = [".#.",
#         "..#",
#         "###"]
cycle_num = 6
#cycle_num = 3 

cycle_num = cycle_num + 1

#Print Output
def display_cube(cube):
    print(str(len(cube)) + " " + str(len(cube[0])) + " " + str(len(cube[0][0])))
    for j in range(1, len(cube) - 1):
        print('-'*10 + " z=" + str(j-cycle_num))
        for i in range(1, len(cube[j]) - 1):
            print( cube[j][i][1:len(cube[j][i]) -1] )


def count_activated(cube):
    count = 0
    for plane in cube:
        for line in plane:
            for pixel in line:
                if pixel == '#':
                    count += 1
    return count

#Create Conway Cube Space
blank_lines = "." * ( cycle_num * 2 + len(start[0]) )
blank_canvas = [ copy.deepcopy(blank_lines) for i in range(len(start) + cycle_num * 2) ]
work_canvas = [ copy.deepcopy(blank_lines) if ((i - cycle_num) < 0 or (i - cycle_num) >= len(start)) 
        else ( "." * cycle_num + start[i - cycle_num] + "." * cycle_num) 
        for i in range(len(start) + cycle_num * 2) ]
work_space = [ copy.deepcopy(work_canvas) if ( i - cycle_num ) == 0 else copy.deepcopy(blank_canvas) for i in range(cycle_num * 2 + 1) ]

neighbours_pos = list(product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1]))
neighbours_pos.remove((0,0,0))

#Live cycles
for c in range(cycle_num - 1):
    x = 0
    y = 0
    z = 0
    comparison_space = copy.deepcopy(work_space)
#    display_cube(comparison_space)
#    display_cube(work_space)
#    print('>'*30)
    for z in range(1, len(comparison_space) - 1):
        for y in range(1, len(comparison_space[0]) - 1):
#            print(work_space[z][y])
            newline = comparison_space[z][y]
            for x in range(1, len(comparison_space[0][0]) - 1):
                neighbourhood = sum([ 1 if comparison_space[z+n[0]][y+n[1]][x+n[2]] == '#' else 0 for n in neighbours_pos])
                if(comparison_space[z][y][x] == '#' and not(neighbourhood == 2 or neighbourhood == 3)):
#                    print("# -> .")
#                    print("Before change : " + work_space[z][y])
                    newline = newline[:x] + '.' + newline[x+1:]
#                    print("After  change : " + work_space[z][y])

                if(comparison_space[z][y][x] == '.' and neighbourhood == 3):
#                    print(". -> #")
#                    print("Before change : " + work_space[z][y])
                    newline = newline[:x] + '#' + newline[x+1:]
#                    print("After  change : " + work_space[z][y])

#                print(" x : " + str(x) + " y : " + str(y) + " z : " + str(z) + " sum : " + str(neighbourhood) + " " + comparison_space[z][y][x] + " -> " + work_space[z][y][x])
            work_space[z][y] = newline
#            print(work_space[z][y])
#    print('#' * 20 + " " + str(c+1) + " " + '#' * 20)
#    display_cube(work_space)    
#    print('<'*30)

display_cube(work_space)
print(count_activated(work_space))
