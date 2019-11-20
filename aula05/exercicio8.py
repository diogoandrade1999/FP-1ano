N = int(input("N= "))

while N <= 0:
	print("Número Inválido")
	N = int( input("Número inteiro positivo: ") )

def ndigitos(N):
	counter = 1
	
	while N > 9:
		counter += 1
		N = N // 10
		
	return counter
	
print(ndigitos(N))
