lista = []
for i in range(0,100):
	number = int(input())
	lista.append(number)
	
print(max(lista))
print(lista.index(max(lista))+1)
