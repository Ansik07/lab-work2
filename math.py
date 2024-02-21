#ex1
import math
def deg_to_rad(degree):
    print("In radians its: ",(math.pi/180)*degree)
deg_to_rad(int(input("Enter degree: ")))

#ex2
import math
def area_Trapezoid(h,b1,b2):
    print("Expected output: ", ((b1+b2)/2)*h)
area_Trapezoid(int(input("Enter height: ")), int(input("Base, first value: ")),int(input("Base, second value: ")))

#ex3
import math
def area_polygon(sides,length):
    numerator=sides*(length**2)
    denominator=4*math.tan(math.pi/sides)
    print(int(numerator/denominator))
area_polygon(int(input("Input number of sides: ")), int(input("Input the length of a side: ")))

#ex4
import math
def area_parall(b,h):
    print("Expected output: ",(b*h))
area_parall(int(input("Length of base: ")),int(input("Height the length of a side: ")))

