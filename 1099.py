for i in range(0,int(input())):
	number = input().split()
	suma = 0
	if(number[0] > number [1]):	
		for i in range(int(number[1])+1, int(number[0])):
			if(i % 2 == 1):
				suma+=i
	else:
		for i in range(int(number[0])+1, int(number[1])):
			if(i % 2 == 1):
				suma+=i
						
	print(suma)
