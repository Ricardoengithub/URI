number = int(input())

if(number > 5):	
	for i in range(2, number+1):
		if(i % 2 == 0):
			print(str(i) + "^2 = " + str(i**2))
