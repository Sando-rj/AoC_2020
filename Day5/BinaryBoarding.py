file = open("input.txt",'r')
tab = [n.strip() for n in file.readlines()]

tab.sort()

# Part 1 : Finding Highest seat 

max_seat = tab[0] 
max_seat_row = int(max_seat[:7].replace("B", "1").replace("F", "0"), 2)
max_seat_col = int(max_seat[7:].replace("R", "1").replace("L", "0"), 2)
max_seat_id = max_seat_row * 8 + max_seat_col

print("Maximum seat : " + str(max_seat_id))

# Part 2 : Finding your seat
# 865 found from Part 1

id_tab = [ False for i in range(865) ]

for ticket in tab:    
    row = int(ticket[:7].replace("B","1").replace("F","0"), 2)
    column = int(ticket[7:].replace("R", "1").replace("L", "0"), 2)
    
    id_tab[row * 8 + column] = True

i = 1
while i < 865 and not(id_tab[i - 1] == True and id_tab[i] == False and id_tab[i + 1] == True):
    i = i + 1

print("Your seat is : " +str(i))

