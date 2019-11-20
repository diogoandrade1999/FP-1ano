num = int( input("Número inteiro positivo: ") )

while num <= 0:
	print("Número Inválido")
	num = int( input("Número inteiro positivo: ") )

teste = True

for i in range(2, num):
	primo = num % i
	
	if primo == 0:
		teste = False


if teste == False or num == 1:
        print("Número não Primo")
else :
        print("Número primo")

