a = int(input())
b = int(input())

suma = 0
if(a < b):
	for i in range(a+1,b+1):
		if(i % 2 == 1):
			suma+=i
else:
	for i in range(b+1, a):
		if(i % 2 == 1):
			suma+=i
print(suma)			
