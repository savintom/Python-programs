print("ax^2 + bx + c = 0")
import cmath
a=float(input("enter the value of a : "))
b=float(input("enter the value of b : "))
c=float(input("enter the value of c : "))
d=b**2-4*a*c
sol1=(-b+cmath.sqrt(d))/(2*a)
sol2=(-b-cmath.sqrt(d))/(2*a)
print("the roots are :",sol1,sol2)