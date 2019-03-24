days = int(input())
calendar = [365, 30, 1]
output = []
for i in range(0, len(calendar)):
	tmp = days // calendar[i]
	days-=tmp*calendar[i]
	output.append(tmp)

print(str(output[0]) + " ano(s)")
print(str(output[1]) + " mes(es)")
print(str(output[2]) + " dia(s)")	
