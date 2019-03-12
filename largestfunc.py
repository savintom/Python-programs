def max(a,b,c):
	if a>b and a>c:
		return a
	elif b>a and b>c:
		return b
	else:
		return c
print("enter three numbers: ")
a=input()
b=input()
c=input()
print("the largest of the 3 numbers is ",max(a,b,c))


