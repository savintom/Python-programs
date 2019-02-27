l=['hi','123','savin']
while True:
	print(l)
	c=input("enter the the element u want to add in the list or press q to exit")
	if c=='q':
		print("bye!")
		exit()
	else:
		l.append(c)