class Test:
	h=0
	def __init__(self):
		self.h=6
	def my_func(self,k):
		print("hi,i am in class")
		self.h=k
		print(self.h)
s=Test()
s1=Test()
print(s.h)
print(s1.h)
s.my_func(2)
s1.my_func(4)