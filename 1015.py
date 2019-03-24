import math

def distancia(x1, y1, x2, y2):
	return math.sqrt((x2-x1)**2 + (y2 - y1)**2)

one = input()
two = input()
one = one.split()
two = two.split()
print("{:.4f}".format(distancia(float(one[0]), float(one[1]), float(two[0]), float(two[1]))))
