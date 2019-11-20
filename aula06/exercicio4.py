moedas = [2,2,2,2,2,2,2,2]

def troco(preco_apagar, valor_dado, moedas):
	tipo = [1,2,5,10,20,50,100,200]

	x = valor_dado - preco_apagar

	while x < 0:
		print("Falta Dinheiro!!! {} Centimos".format(-x))
		z = int(input("Quanto dinheiro já deu? "))
		x = z - preco_apagar

	if x == 0:
			print("Deu a quantia certa.")
	else:
		print("Troco:",x)
		while x >= 200 and moedas[7] != 0:
			x = x - 200
			moedas[7] = moedas[7] - 1
		while x >= 100 and moedas[6] != 0:
			x = x - 100
			moedas[6] = moedas[6] - 1
		while x >= 50 and moedas[5] != 0:
			x = x - 50
			moedas[5] = moedas[5] - 1
		while x >= 20 and moedas[4] != 0:
			x = x - 20
			moedas[4] = moedas[4] - 1
		while x >= 10 and moedas[3] != 0:
			x = x - 10
			moedas[3] = moedas[3] - 1
		while x >= 5 and moedas[2] != 0:
			x = x - 5
			moedas[2] = moedas[2] - 1
		while x >= 2 and moedas[1] != 0:
			x = x - 2
			moedas[1] = moedas[1] - 1
		while x >= 1 and moedas[0] != 0:
			x = x - 1
			moedas[0] = moedas[0] - 1

		if x != 0:
			print("Não tenho troco suficiente")
		else:
			print("Entregue ", end="")
			for k in range(len(moedas)):
				if moedas[k] != 2:
					if tipo[k] != 100 and tipo[k] != 200:
						print(2-moedas[k],"x",tipo[k],"Centimos ", sep="", end="")
					else:
						print(2-moedas[k],"x",int(tipo[k]/100),"Euros ", sep="", end="")

a = int(input("Preço: "))
b = int(input("valor dado: "))	
troco(a, b, moedas)