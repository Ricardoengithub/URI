def mayor(a, b):
	return (a + b + abs(a - b))//2
	
line = input()
line = line.split()
print(mayor(mayor(int(line[0]), int(line[1])),int(line[2])), "eh o maior")

