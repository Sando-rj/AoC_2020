# Part 1 : 2020th number
# Rules if i - 1 new, i = 0
#       else actual_turn - occur(i)

occurences = dict()

input_num = [1, 20, 8, 12, 0, 14]
next_num = -1

#Part 1 goal
goal_turn = 2020
#Part 2 goal
goal_turn = 30000000

for i in range(1, goal_turn + 1):
    if (i - 1) < len(input_num):
        occurences[next_num] = i
        next_num = input_num[i - 1]
    else:
        if next_num in occurences.keys():
            tmp = i - occurences[next_num]
            occurences[next_num] = i
            next_num = tmp
        else:
            occurences[next_num] = i
            next_num = 0

    if(i%300000 == 0):
        print("Round " + str(i) + " : " + str(next_num) + " " + str(int(i/300000)) + "% ")
