def simple(p,r,t):
	if p<0 or r<0 or t<0:
		print("invalid input")
		exit()
	si=(p*r*t)/100
	return si

print("SIMPLE INTEREST PROGRAM")
p=float(input("enter the principal amount: "))
r=float(input("enter the rate of interest (in percentage): "))
t=float(input("enter the time period (in years)"))

print("the simple interest is:",simple(p,r,t))