sav=[]
print(sav)

savlist=['hi','bro',777,'!!!','how are u?']
print(savlist)

print(savlist[0])
print(savlist[4])

for i in savlist:
	print(i)

savlist[0]='hiiiiii'
print(savlist)

print("length of the list is ",len(savlist))

if 9 in savlist:
	print("9 is there")
elif 'bro' in savlist:
	print("'bro' is there")

for i in range(4):
	print(i)

import random
r=random.randint(1,6)
print(r)

r=random.choice(savlist)
print(r)

savlist=[1,2,3]
l=[4,5,6]
savlist.append(l)
print(savlist)
