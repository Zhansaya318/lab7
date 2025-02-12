import math

#task 1
n = int(input("Input degree: "))
print("Output radian:", math.radians(n))

#task 2
h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))

print("Expected Output:", h/2 * (a + b))

#task 3
n = int(input("Input number of sides: "))
s = int(input("Input the length of a side: "))
a = s/2*math.tan(math.pi/n)
print("The area of the polygon is:", n*a*s/2)

#task 4
B = int(input("Length of base: "))
H = int(input("Height of parallelogram: "))
print("Expected Output:", B*H)