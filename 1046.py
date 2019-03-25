lista = input().split()
lista[1] = int(lista[1])
lista[0] = int(lista[0])

horas = (lista[1]-lista[0]) % 24
if(horas == 0):
	horas = 24
print("O JOGO DUROU "+ str(horas) +" HORA(S)")
