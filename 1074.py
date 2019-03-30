for i in range(0, int(input())):
	number = int(input())
	if(number == 0):
		print("NULL")
	else:
		if(number < 0):
			if( number % 2 == 0):
				print("EVEN NEGATIVE")
			else:
				print("ODD NEGATIVE")
		else:
			if(number > 0):
				if(number % 2 == 0):
					print("EVEN POSITIVE")
				else:
					print("ODD POSITIVE")
