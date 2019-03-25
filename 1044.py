lista = input().split()
lista[1] = int(lista[1])
lista[0] = int(lista[0])

if(lista[1] % lista[0] == 0 or lista[0] % lista[1] == 0):
	print("Sao Multiplos")
else:
	print("Nao sao Multiplos")
