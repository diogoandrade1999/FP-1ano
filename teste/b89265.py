#Diogo André Lopes Andrade 89265

def energia(massa, velocidade):
	energiac = 0.5 * massa * velocidade**2
	return energiac

def mensagem(energiac):
	if energiac < 1000:
		print("Baixa")
	elif 1000 <= energiac <= 5000:
		print("Média")
	else:
		print("Alta")
		
def lerValorRealPositivo():
	velocidade = int(input("Velocidade (m/s)? "))
	while velocidade <= 0:
		velocidade = int(input("Número inválido! Velocidade (m/s)? "))
	return velocidade

def menu():
	print("Opções disponiveis:")
	print("0 - sair")
	print("1 - introduzir nova medida")
	print("2 - mostrar média atual")
	
	opcao = int(input("Opção? "))
	
	media = 0
	count = 0
	
	if opcao == 0:
		print("Fim")
		print("Até Breve")
	elif opcao == 1:
		massa = float(input("Massa (kg)? "))
		a = energia(massa, lerValorRealPositivo())
		count += 1
		media = (media + a) / count
		print(a)
		mensagem(a)
	elif opcao == 2:
		if media == 0:
			print("Média atual: ", media)
			print("Ainda não foram inroduzidas medidas!")
		else:
			print("Média atual: ", media)
			msg = """ Média da energia para {} corpos: """
			print(msg.format(count), media)
	else:
		print("Opção inválida")
	
	return opcao

print("Calculadora da Energia Cinética","\n")

while menu() != 0:
	menu()




