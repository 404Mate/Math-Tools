from math import sqrt 
import numpy as np
import sys

def main():
    toolselect = input("""What tool do you need?
    1: Circle Area
    2: Cone Volume
    3: Cylinder Surface Area
    4: Point Distance
    5: Rectangular Prism
    6: Trapezoid Area
    7: Area between concentric circles
    8: numpy arrays
    """)

    if toolselect == "1":
        radius = float(input("What is your radius?\n"))
        print("Your circle's area is", radius ** 2 * 3.14, "\n")
        print("Your circle's circumfrence is", 2 * radius * 3.14, "\n")
    elif toolselect == "2":
        radius = float(input("What is your radius?\n"))
        height = float(input("What is your height?\n"))
        print("Your volume is: ", radius ** 2 * 3.14 * height / 3, "\n")
    elif toolselect == "3":
        radius = float(input("What is your radius?\n"))
        height  = float(input("What is your height?\n"))
        print("Your surface area is:", height * 2 * radius * 3.14 + (2 * 3.14 * radius ** 2), "\n")
    elif toolselect == "4":
        x1 = float(input("X1\n"))
        y1 = float(input("Y1\n"))
        x2 = float(input("X2\n"))
        y2 = float(input("Y2\n"))
        print("The distance is the square root of", (x2 - x1) ** 2 + (y2 - y1) ** 2, "or", sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), "\n")
    elif toolselect == "5":
        length = float(input("What is your length?\n"))
        width = float(input("What is your width?\n"))
        height = float(input("What is your height?\n"))
        print("Your volume is:", length * width * height, "\n")
        print("Your surface area is:", (width * height * 2) + (width * length * 2) + (length * height * 2), "\n")
    elif toolselect == "6":
        top = float(input("Top base\n"))
        bottom = float(input("Bottom Base\n"))
        height = float(input("Height\n"))
        print("The area of your trapazoid is:", (height / 2) * (top + bottom), "\n")
    elif toolselect == "7":
        big = float(input("Big circle\n"))
        small = float(input("Small Circle\n"))
        print("The area is", 3.14 * big ** 2 - 3.14 * small ** 2)
        elif toolselect == "8":
            ary = np.array([1, 2, 3, 4])  # array([1, 2, 3, 4])

ary[0]  # 1
ary[2]  # 3
ary[::2]  # array([1, 3])




np.array([1, 2, 3, 4], dtype=np.float32)
# array([1., 2., 3., 4.], dtype=float32)



arr = np.array([1, 2, 3, 4])
print(arr.dtype) # dtype('int64')
arr.dtype = np.float32
print(arr)
# [1.e-45 0.e+00 3.e-45 0.e+00 4.e-45 0.e+00 6.e-45 0.e+00]



arr = arr.astype(np.float32)
print(arr)
    else:
        print("Sorry that was not recognized\n")
        sys.exit()

if __name__ == "__main__":
    main()

#---------------------------
#  Made by 404Mate with <3  
#--------------------------- 
