num = float( input("Escreva o  número zero: ") )
soma = 0
media = 0
elementos = 0
maximo = num
minimo = num


while num != 0:
	soma = soma + num
	elementos = elementos + 1
	media = soma / elementos
	
	if maximo < num:
		maximo = num
	
	if minimo > num:
		minimo = num
			
	num = float( input("Escreva o  número zero: ") )		
			
print("Soma: ",soma,"Número de elementos: ",elementos,"Média: ",media,"Máximo: ",maximo,"Mínimo: ",minimo)

