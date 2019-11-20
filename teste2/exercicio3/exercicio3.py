import time

def base_dados():
	ficheiro = open('hipermercado.txt', 'r')
	a = {}
	for line in ficheiro:
		code, nome, seccao, preco, iva = line.strip().split(';')
		b = [code, nome, seccao, preco, iva]
		if code not in a:
			a[code] = ''
		a[code] = b
	ficheiro.close()
	return a

def guardar(total_produtos,vendas):
	ficheiro = open('vendas.txt', 'a')
	for x in range(len(vendas)):
		ficheiro.write(vendas[x][0]+' : '+str(vendas[x][1])+'\n')
	ficheiro.close()
	ficheiro = open('stockout.txt', 'w')
	codigo = total_produtos.keys()
	for line in codigo:
		ficheiro.write(line+';'+total_produtos[line]+'\n')
	ficheiro.close()

def total_produtos(produto):
	codigos = produto.keys()
	d = {}
	for x in codigos:
		d[x] = '0'
	return d

def main():
	print("(I)nserir Itens")
	print("(F)aturar")
	print("(S)air")
	escolha = input("> ")
	return escolha

produto = base_dados()
total_produtos = total_produtos(produto)
vendas = []
while True:
	y = main()
	if y.lower() == 'i':
		compras = {}
		venda = []
		total = 0
		codigo = input("Cófigo: ")
		while codigo != '0':
			if codigo in produto:
				iv = produto[codigo][4][:-1]
				prec = float(produto[codigo][3])+float(produto[codigo][3])*(float(iv)/100)
				total = total + prec
				print(produto[codigo][1],"%.2f" % prec)
				prod = int(total_produtos[codigo]) + 1
				total_produtos[codigo] = str(prod)
				if produto[codigo][2] not in compras:
					compras[produto[codigo][2]] = []
				compra = [produto[codigo][1], produto[codigo][3], produto[codigo][4]]
				compras[produto[codigo][2]].append(compra)
			else:
				print("Produto inválido")
			codigo = input("Cófigo: ")	
		print()
		tempo = time.strftime("%d/%m/%Y %H:%M")
		venda.append(tempo)
		venda.append(total)
		vendas.append(venda)
	elif y.lower() == 'f':
		valor_liquido = 0
		valor_bruto = 0
		valor_iva = 0
		print()
		for x in compras:
			a = 1
			print(x,':')
			for l in range(len(compras[x])):
				print("{:>5d} {:<15s} ({:^3s}) {:^4.2}€".format(a, compras[x][l][0], compras[x][l][2][1:],float(compras[x][l][1])))
				a += 1
				iv = compras[x][l][2][:-1]
				valor_liquido = valor_liquido + (float(compras[x][l][1])+float(compras[x][l][1])*(float(iv)/100))
				valor_iva = valor_iva + (float(compras[x][l][1])*(float(iv)/100))
				valor_bruto = valor_bruto + (float(compras[x][l][1]))
		print()
		print("Total Bruto:","%.2f" % valor_bruto)
		print("Total IVA:","%.2f" % valor_iva)
		print("Total Liquido:","%.2f" % valor_liquido)
		print()
	elif y.lower() == 's':
		guardar(total_produtos, vendas)
		print()
		break
	else:
		print("escolha inválida")
		print()