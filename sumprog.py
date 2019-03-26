a=int(input("enter 1st value"))
b=int(input("enter 2nd value"))
c=int(input("enter 3rd value"))
def sum(a,b,c):
	sum=a+b+c
	if a==b or b==c or a==c:
		sum=0
	return sum
print("the sum is: ",sum(a,b,c))