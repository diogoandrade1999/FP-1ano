N = float(input("Número: "))

def soma(N):
	a = True
	k = N
	
	while a == True:
		X = float(input("Número(se quiser parar digite 0): "))
		
		k = k + X
		
		if X == 0:
			a = False
		
	return k
	
print("Soma=",soma(N))
