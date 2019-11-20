fic = open('texto.csv', 'r')
fic.readline()

l = []

def ler(l):
	for line in fic:
		lista = []
		for word in line.split(','):
			lista.append(word.rstrip())
		l.append(lista)
	return l
	
def main():
	print('1-Número mecanográfico')
	print('2-Nome')
	print('3-turma')
	print('4-API')
	print('5-APT')
	
	x = input('Escolha: ')
	
	print('A-Ordem crescente')
	print('B-Ordem decrescente')
	
	y = input('Escolha: ')
	
	return x,y
	
	
main()
print(ler(l))
	
fic.close()
