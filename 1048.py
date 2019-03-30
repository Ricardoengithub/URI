number = float(input())

ganar = 0
salario =0
if(number > 2000):
	ganar = (number*1.04)-number
	salario = number * 1.04
else:
	if(number > 1200):
		ganar = (number*1.07)-number
		salario = number * 1.07
	else:
		if(number > 800):
			ganar = (number*1.1)-number
			salario = number * 1.1
		else:
			if(number > 400):
				ganar = (number*1.12)-number
				salario = number * 1.12
			else:
				ganar = (number*1.15)-number
				salario = number * 1.15				

print("Novo salario: {:.2f}".format(salario))
print("Reajuste ganho: {:.2f}".format(ganar))
print("Em percentual: {:.0f} %".format(((salario/number)-1)*100))
