contador = 0
contador2 = 0
for i in range(0,int(input())):
	numero = int(input())
	if(numero >= 10 and numero <= 20):
		contador+=1
	else:
		contador2+=1
		
print(str(contador) + " in")
print(str(contador2) + " out")		
