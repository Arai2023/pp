import math
sides = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
P = length*sides
x = math.tan(180/sides)
Alpha = length/(2*x)
S = (P*Alpha)/2
print(S)