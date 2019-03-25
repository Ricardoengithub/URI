price = [4,4.5,5,2,1.5]

line = input()
line = line.split()

print("Total: R$ {:.2f}".format(price[int(line[0])-1]*int(line[1])))
