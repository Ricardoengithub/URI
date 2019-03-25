number = float(input())
intervalos = ["[0,25]", "(25,50]", "(50,75]", "(75,100]"]
if(number < 0 or number > 100):
	print("Fora de intervalo")
else:
	if(number <= 25):
		print("Intervalo", intervalos[0])
	else:
		if(number <= 50):
			print("Intervalo", intervalos[1])
		else:
			if(number <= 75):
				print("Intervalo", intervalos[2])
			else:
				if(number <= 100):
					print("Intervalo", intervalos[3])				
	
