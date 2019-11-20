l = []
i = 1

def calcular(l):
	k = 2 + (len(l) - 2) * (len(l) + 1)
	print("Existem {} confrontos.".format(k))

	if k != 0:
		for x in range(len(l)):
			y = x + 1
			if y < len(l):
				print(l[x],"-",l[y])
				print(l[y],"-",l[x])
			else:
				y = 0
				print(l[x],"-",l[y])
				print(l[y],"-",l[x])


z = int(input("Quantas equipas quer que entrem em confronto: "))

while i <= z:
	x = input("Insira equipas: ")
	l.append(x)
	i += 1

print(l)
calcular(l)