import random
print("ROCK, PAPER, SCISSOR GAME!!!")
uscore=0
cscore=0
while True:
	d={'r':'rock','p':'paper','s':'scissor'}
	print(d)
	p=input("enter your choice ('r' for rock ,'p' for paper , 's' for scissor) and press 'q' to exit :")
	r=random.choice(['r','p','s'])
	
	if p=='q':
		print("bye!")
		exit()
	elif p != 'r' and p != 's' and p != 'p':
		print("invalid input, try again")
	else:
		p=d[p]
		r=d[r]
		print("computer chose ",r)
	if p==r:
		print("computer chose ",p,"tie, try again")
		print("your score is ",uscore)
		print("computer score is ",cscore)
	elif p==d['r'] and r==d['p']:
		print("you lose!")
		cscore=cscore+1
		print("your score is ",uscore)
		print("computer score is ",cscore)
	elif p==d['r'] and r==d['s']:
		print("you win!")
		uscore=uscore+1
		print("your score is ",uscore)
		print("computer score is ",cscore)
	elif p==d['p'] and r==d['r']:
		print("you win!")
		uscore=uscore+1
		print("your score is ",uscore)
		print("computer score is ",cscore)
	elif p==d['p'] and r==d['s']:
		print("you lose!")
		cscore=cscore+1
		print("your score is ",uscore)
		print("computer score is ",cscore)
	elif p==d['s'] and r==d['r']:
		print("you lose!")
		cscore=cscore+1
		print("your score is ",uscore)
		print("computer score is ",cscore)
	elif p==d['s'] and r==d['p']:
		print("you win!")
		uscore=uscore+1
		print("your score is ",uscore)
		print("computer score is ",cscore)
	if uscore==3:
		print("you win!!,game over")
		exit()
	elif cscore==3:
		print("computer wins!!,game over")
		exit()
	
