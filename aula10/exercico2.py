fic = open('texto.csv', 'r')

l = []

#fic.readline()

for line in fic:
	print(line)
	lista = []
	lista.append(line)
	#print(lista)
	l.append(lista)
	
fic.close()

#print(l)
