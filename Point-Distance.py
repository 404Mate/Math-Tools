from math import sqrt

x1 = input("X1\n")
y1 = input("Y1\n")
x2 = input("X2\n")
y2 = input("Y2\n")

part1 = float(x2) - float(x1)
part2 = float(y2) - float(y1)

part1 = part1 * part1 
part2 = part2 * part2


print("The distance is the square root of", part1 + part2, "or", sqrt(part1 + part2))

#---------------------------
#  Made by 404Mate with <3  
#--------------------------- 
