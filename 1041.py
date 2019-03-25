x = input().split()
y = float(x[1])
x = float(x[0])

if(y == 0):
	if(x == 0):
		print("Origem")
	else:
		print("Eixo X")
else:
	if(x == 0):
		if(y != 0):
			print("Eixo Y")
	else:
		if(x > 0):
			if(y > 0):
				print("Q1")
			else:
				print("Q4")
		else:
			if(y > 0):
				print("Q2")
			else:
				print("Q3")
