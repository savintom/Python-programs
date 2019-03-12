print("STANDARD EXCEPTIONS, TRY AND EXCEPT")
try:
	d=int(input("enter a number"))
	if d==5:
		raise NameError
	elif d>5:
		raise TypeError
except NameError:
	print("error!,you entered a number equal to 5")
except TypeError:
	print("error!, you entered a number greater than 5")
else:
	print("no error, you entered",d)
finally:
	print("program completed!!!")