def menu():
	print()
	print("1) Registar chamada")
	print("2) Ler ficheiro")
	print("3) Listar clientes")
	print("4) Fatura")
	print("5) Terminar")
	escolha = int(input("Opção: "))
	print()
	return escolha

def n_tel(text):
	while True:
		x = input(text)
		if (len(x) >= 3 and x.isdigit()) or (len(x) >= 4 and x[0] == '+' and x[1:].isdigit()):
			break
		else:
			print("Número inválido")
	return x

def registar_chamada():
	origem = n_tel("Número de Origem: ")
	destino = n_tel("Número de Destino: ")
	duracao = int(input("Duração (s): "))
	return origem, destino, duracao

def ler_ficheiro(nome, chamadas):
	try:
		ficheiro = open(nome, 'r')
		for line in ficheiro:
			n_origem, n_destino, duracao = line.strip().split(' ')
			chamada = (n_origem, n_destino, int(duracao))
			cliente = chamada[0]
			if cliente not in chamadas:
				chamadas[cliente] = []
			chamadas[cliente].append(chamada)
		ficheiro.close()	
	except FileNotFoundError:
		print("Ficheiro inválido")

def custo(lista):
	if lista[1][0] == '2':
		preco = 0.02
	elif lista[1][0] == '+':
		preco = 0.8
	elif lista[1][0] == lista[1][1]:
		preco = 0.04
	else:
		preco = 0.1
	cust = (lista[2] /60) * preco
	return cust

def fatura(cliente, chamadas):
	print("Fatura do cliente: ", cliente)
	print("{:<20s} {:>8s} {:>10s}".format("Destino", "Duração", "custo"))
	lista = chamadas[cliente]
	for line in lista:
		cust = custo(line)
		print("{:<20s} {:>8d} {:>10.2f}".format(line[1], line[2],cust))

chamadas = {}
while True:
	y = menu()
	if y == 1:
		chamada = registar_chamada()
		cliente = chamada[0]
		if cliente not in chamadas:
			chamadas[cliente] = []
		chamadas[cliente].append(chamada)
	elif y == 2:
		nome = input("Nome do ficheio: ")
		ler_ficheiro(nome, chamadas)
	elif y == 3:
		clientes = sorted(chamadas.keys())
		print("Clientes: ", end="")
		for x in clientes:
			print(x, end=' ')
		print()
	elif y == 4:
		 cliente = input("Cliente: ")
		 if cliente not in chamadas:
		 	print("Cliente inválido")
		 else:
		 	fatura(cliente, chamadas)
	elif y == 5:
		break
	else:
		print("Opção inválida")