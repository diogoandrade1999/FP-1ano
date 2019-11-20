N = int( input("Número inteiro positivo: ") )
soma = 0
a = []

while N <= 0:
	print("Número Inválido")
	N = int( input("Número inteiro positivo: ") )

for i in range(1, N):
	divisor = N % i
	
	if divisor == 0:
            soma = soma + i
            a.append(i)

if soma > N:
    print("Número Abundante e os seus divisores são",a)
elif soma < N:
    print("Número Defeciente e os seus divisores são",a)
else :
    print("Número Perfeito e os seus divisores são",a)
