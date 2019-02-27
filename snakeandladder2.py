import random
d=0
p=0
snl={11:2,13:34,25:4,8:37,38:9,40:68,65:46,52:81,93:64,97:76,89:70}
def rolldice():
	return random.randint(1,6)
while True:
	r=input("press r to roll , q to quit : ")
	if r == 'r':
		d=rolldice()
		print("you got : ",d)
		if d == 6 or d==1:
			p=d
			print("congratulations, your in the game!")
			print("you start on ",p)
			break
		else:
			print("you need to get 6 or 1 to start. try again")
	elif r=='q':
		exit()
while True:
	r=input("press r to roll , q to quit : ")
	if r == 'r':
		d=rolldice()
		print("you got : ",d)
		p=p+d
		if p>100:
			p=p-d
			print("you need to get ",100-p," to reach home.")
		print("your new position is : ",p)
		if p==100:
			print("Hurray!,you won!")
			exit()
		if p in snl:
			if p<snl[p]:
				print("wow, you got a ladder")
			else:
				print("ooops, you got bitten by a snake")
			p=snl[p]
			print("move to ",p)
	elif r=='q':
		print("bye!")
		exit()