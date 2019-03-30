rates = [0,0,0,0]
for i in range(0,5):
	number = int(input())
	if(number % 2 == 0):
		rates[0]+=1		
	else:
		rates[1]+=1
	if(number > 0):
		rates[2]+=1
	else:
		if(number != 0):
			rates[3]+=1
		
print(str(rates[0]) + " valor(es) par(es)")
print(str(rates[1]) + " valor(es) impar(es)")
print(str(rates[2]) + " valor(es) positivo(s)")
print(str(rates[3]) + " valor(es) negativo(s)")
