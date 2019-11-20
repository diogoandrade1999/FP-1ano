import sys

dic = {}
arquivo = open(sys.argv[1], 'r')

for line in arquivo:
	for letra in line.lower():
		if letra.isalpha():
			if letra in dic:
			  dic[letra] += 1
			else:
			  dic[letra] = 1

arquivo.close()

print(dic)
