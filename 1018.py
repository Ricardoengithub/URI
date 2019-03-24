value = int(input())
notes = [100, 50, 20, 10, 5, 2, 1]
print(value)
for i in range(0,len(notes)):
	tmp = value // notes[i]
	print(str(value // notes[i]) + " nota(s) de R$ "+ str(notes[i])+ ",00")
	value-= tmp*notes[i] 
