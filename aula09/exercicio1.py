x = input("Nome do ficheiro: ")
l = []

arquivo = open(x, 'r')

for line in arquivo:
	l.append(float(line.rstrip()))

arquivo.close()

print("%.2f" % sum(l))
