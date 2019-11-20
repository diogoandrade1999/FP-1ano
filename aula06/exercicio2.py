tel = ['5','2','3','5']
nome = ['Mariana','Maria','Marta','Marisa']

def correspondencia(tel, nome, x):
	verifica = False
	for i in range(len(tel)):
		if tel[i] == x:
			print("Este número pertence a",nome[i])
			verifica = True
	if verifica == False:
		print("Não há correspondencia:",x)	
	return

def parte(tel, nome, y):
	verifica = False
	for i in range(len(nome)):
		if y.upper() in nome[i].upper():
			print("O número",tel[i],"é da",nome[i])
			verifica = True
	if verifica == False:
		print("Não há correspondencia:",y)	
	return

x = input("Telefone: ")
correspondencia(tel, nome, x)
y = str(input("Nome: "))
parte(tel, nome, y)