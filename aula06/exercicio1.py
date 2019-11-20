def tamanho(lista):
	a = 0
	for i in lista:
		a += 1
	print("Tamanho da lista é: ",a)
	return a
	
def lista():
	lista = []
	x = True
	while x:
		n = input("Números: ")
		if n != '':
			lista.append(int(n))
		else:
			break
	print(lista)
	return lista

def soma(lista):
	x = 0
	for i in lista:
		x = x + i
	print("Soma:", x)
	return x
	
def n_elementos(n, lista):
	count = 0
	for i in lista:
		if i < n:
			count += 1
	print("Os números inferiores a {} são:".format(n), count)
	return count
	
def maximo(lista):
	x = True
	k = 0
	for i in lista:
		if x:
			z = i
			x = False
		else:
			if z < i:
				z = i
	for i in lista:
		if z/2 > i:
			k += 1
	print("O máximo é: ", z)
	print("Os números inferiores a metade do máximo são: ", k)
	return z, k

def troca(lista):
	lista2 = []
	x = int(input("Qual é o elemento que pretende substituir: "))
	k = int(input("Qual é o elemento que pretende colocar: "))
	for i in lista:
		if i == x:
			lista2.append(k)
		else:
			lista2.append(i)
	print (lista2)
	return lista2

def inversa(lista):
	lista3 = []
	for i in lista:
		lista3.insert(0, i)
	print (lista3)
	return lista3


y = lista()
tamanho(y)
soma(y)
n= int(input("número para max: "))
n_elementos(n, y)
maximo(y)
troca(y)
inversa(y)
print(y)
