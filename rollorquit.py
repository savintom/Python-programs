import random
while True:
	r=input("press r to roll,q to quit")
	if r == 'r':
		print(random.randint(1,6))
	elif r == 'q':
		print("bye!")
		exit()
print("finish")