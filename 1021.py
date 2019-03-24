value = float(input())
notes = [100, 50, 20, 10, 5, 2]
coins = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
print("NOTAS:")
for i in range(0,len(notes)):
	tmp = value // notes[i]
	print(str(round(value // notes[i])) + " nota(s) de R$ "+ str(notes[i])+ ".00")
	value-= tmp*notes[i] 
	
print("MOEDAS:")
for i in range(0,len(coins)):
	tmp = value // coins[i]
	print(str(round(value // coins[i])) + " moeda(s) de R$ "+ str("{:.2f}".format(coins[i])))
	value-= tmp*coins[i] 	
