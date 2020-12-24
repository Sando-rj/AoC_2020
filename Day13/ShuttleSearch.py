import math

file = open("input.txt",'r')
tab = [n for n in file.readlines()]

#tab = ["939",
#"7,13,x,x,59,x,31,19"]

timestamp = int(tab[0])
buses = [ n for n in tab[1].strip().split(',') if n != 'x' ]
bus_timestamp = []

min_time = ((int(timestamp / int(buses[0])) + 1) * int(buses[0]))
b_time = buses[0]

for b in buses:
    b_time = ((int(timestamp / int(b)) + 1) * int(b))
    bus_timestamp.append(b_time - timestamp)
    if (b_time - timestamp) < min_time:
        min_b = b
        min_time = b_time - timestamp

print(b_time)
print(" bus id " + str(min_b) + " bus time delta " + str(min_time) + " res : " + str(int(min_b) * min_time) )
