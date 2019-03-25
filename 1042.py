lista = input().split()
tmp = []
for i in range(0, len(lista)):
	tmp.append(int(lista[i]))
tmp.sort()

for i in tmp:
	print(i)
print("")
for i in range(0,3):
	print(lista[i])
