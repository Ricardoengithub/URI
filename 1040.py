A = input()
A = A.split()
##examen = input()
E = ""
B = float(A[1])
C = float(A[2])
D = float(A[3])
try:
	E = float(A[4])
except IndexError:
	pass

A = float(A[0])

tmp = (A*2 + B*3 + C*4 + D)/10


print("Media: {:.1f}".format(tmp))
if(tmp > 7):
	print("Aluno aprovado.")
else:
	if(tmp < 5):
		print("Aluno reprovado.")
	else:
		print("Aluno em exame.")
		
if(E != ""):
	print("Nota do exame:", E)
	if((E+tmp)/2 > 5):
		print("Aluno aprovado.")
		print("Media final:", (E+tmp)/2)
	else:
		print("Aluno reprovado.")
		print("Media final:", (E+tmp)/2)		
