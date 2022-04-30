x ="y"
while(x == "y"):
	try:	
		import random
		
		print("\t\t Start the game ")
		i = 1
		j = 0
		k = 0
		while(i<=10 and j<=10 and k <= 10):
			print("Choice from \"Snake\" , \"Water\"  OR  \"Gun\"")
			a = input().capitalize()
			list1 = ["Snake","Gun","Water"]	
			b = random.choice(list1)
			if a == "Snake":
				if  b == "Water":
					print(b)
					print("You have won\n")
					j = j +1
				elif b == "Gun":
					print(b)
					print("You are dead\n")
					k +=1
				elif b == "Snake" :
					print(b)
					print("Try again\n")
			elif a == "Water":
				if b == "Gun":
					print(b)
					print("You have won\n")
					j = j +1
				elif b == "Snake":
					print(b)
					print("You are dead\n")
					k += 1
				elif b == "Water" :
					print(b)
					print("Try again\n")
			elif a == "Gun":
				if b == "Snake":
					print(b)
					print("You have won\n")
					j = j + 1
				elif b == "Water":
					print(b)
					print("You are dead\n")
					k +=1
				elif b== "Gun":
					print(b)
					print("Try again\n")
			else :
				print("Please Enter valid input")
				continue
			i = i +1
		else:
			print("You have Taken Round \n", (i-1))
			print("You have Won",j)
			print("You have loss",k)
	except Exception as c:
			print(c)
	print("Do you want play again? Type \"y\" or if not Type \"n\":")
	x = input()
else:
	exit()
	
	
	
				