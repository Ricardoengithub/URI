import math
def Fgeneral1(a,b,c):
	try:
		x = (-b + math.sqrt(b**2 - (4*a*c)) ) /(2*a)
		return x
	except ValueError:
		return False
		
def Fgeneral2(a,b,c):
	try:
		x = (-b - math.sqrt(b**2 - (4*a*c)) ) /(2*a)
		return x
	except ValueError:
		return False
		
line = input()
line = line.split()

A = float(line[0])
B = float(line[1])
C = float(line[2])

if(Fgeneral1(A, B, C) != False and Fgeneral2(A, B, C) != False):
	print("R1 = {:.5f}".format(Fgeneral1(A, B, C)))
	print("R2 = {:.5f}".format(Fgeneral2(A, B, C)))
else:
	print("Impossivel calcular")	


