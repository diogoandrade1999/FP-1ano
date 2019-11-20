def lista():
	lst = []
	x = True
	while x:
		n = input("Números: ")
		if n != '':
			lst.append(int(n))
		else:
			break
	print(lst)
	return lst

def remove_e_conta(lista, x):
	lista2 = []
	count = 0
	for i in lista:
		if i == x:
			count += 1
		else:
			lista2.append(i)
	return lista2, count
	
z = lista()
x = int(input("Número: "))
k = remove_e_conta(z, x)
print(k)
print(k[0])
print(k[1])
