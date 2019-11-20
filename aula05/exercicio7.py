N = int(input("N= "))

while N <= 0:
	print("Número Inválido")
	N = int( input("Número inteiro positivo: ") )

def countdown(N):
	a = []
	
	for i in range(1, N+2):
		i = i - 1
		a.insert(0, i)
		
	return a
	
print(countdown(N))
