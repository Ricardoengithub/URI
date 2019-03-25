contador = 0
suma = 0
for i in range(0,6):
	number = float(input())
	if(number > 0):
		suma+=number
		contador+=1
print(str(contador) + " valores positivos")
print("{:.1f}".format(suma/contador))
