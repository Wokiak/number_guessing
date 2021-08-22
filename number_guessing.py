import random
a = int(random.randrange(1,10))
print("a = " ,a)
tries= 0 21
def hint():
	if a > b:
		print("higher")
	elif a < b:
		print("lower")
	if tries > 5 :
		if a % 2 == 0:
			print("a can devide on 2")
			
		if a % 5 == 0:
			print("a can devide on 5")
while True :
	b = int(input("Enter your number :"))
	print(tries)
	if a==b:
		print("success with" , tries , "tries")
		break
	hint()
	tries += 1 


