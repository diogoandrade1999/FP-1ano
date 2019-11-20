l = []

x = input("Ficheiro: ")

fic = open(x, 'r')

for line in fic:
	for palavra in line.split(' '):
		if palavra.lower().isalpha():
			if palavra.lower() not in l:
				l.append(palavra.lower().rstrip())

fic.close()

l2 = sorted(l)

print(l2)
