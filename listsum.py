def listsum():
	list=[]
	sum=0
	print("enter the number of elements in the list")
	n=int(input())
	print("enter the elements of the list")
	for i in range(n):
		d=input()
		list.append(d)
	for i in list:
		sum=sum+int(i)

	print("the sum of the elements of the list is: ",sum)

listsum()
	

