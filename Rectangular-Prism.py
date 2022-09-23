# get dimensions
length = input("what is your length?\n")
width = input("\nwhat is your width?\n")
height = input("\ninputwhat is your height?\n")

# convert it to floats incase there are decimal points in the input
height = float(height)
width = float(width)
length = float(length)

# math time
part1 = width * height * 2
part2 = width * length * 2
part3 = length * height * 2

surfacearea = part1 + part2 + part3
print("\n")
print("your volume is:", length * width * height)
print("your surface area is:", surfacearea)

#---------------------------
#  Made by 404Mate with <3  
#--------------------------- 