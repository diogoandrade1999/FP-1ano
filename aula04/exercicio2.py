import random

num = random.randint(1, 100)

poss = int ( input("Tenta adivinhar o número: ") )

tentativas = 0

while poss != num:
	if poss > num:
		tentativas = tentativas + 1
		print ("Valor Alto")
	
	if poss < num:
		tentativas = tentativas + 1
		print ("Valor Baixo")
		
	
	poss = int ( input("Tenta adivinhar o número: ") )

tentativas = tentativas + 1
print(tentativas)
