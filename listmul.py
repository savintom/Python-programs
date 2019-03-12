def listmul():
	list=[]
	mul=1
	print("enter the number of elements in the list")
	n=int(input())
	print("enter the elements of the list")
	for i in range(n):
		d=input()
		list.append(d)
	for i in list:
		mul=mul*int(i)
	print("the product of the elements of the list is: ",mul)

listmul()