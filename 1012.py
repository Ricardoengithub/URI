def triangulo(a, c):
	return (a * c) / 2.0

def circulo(c):
	return 3.14159 * (c**2)

def trapezio(a, b, c):
	return ((a + b) * c) / 2.0

def cuadrado(b):
	return b * b

def rectangulo(a, b):
	return a * b	
	
A = input()
A = A.split()
A[0] = float(A[0])
A[1] = float(A[1])
A[2] = float(A[2])

print("TRIANGULO: {:.3f}".format( triangulo(A[0], A[2])))
print("CIRCULO: {:.3f}".format(circulo(A[2])))
print("TRAPEZIO: {:.3f}".format(trapezio(A[0], A[1], A[2])))
print("QUADRADO: {:.3f}".format(cuadrado(A[1])))
print("RETANGULO: {:.3f}".format(rectangulo(A[0], A[1])))
