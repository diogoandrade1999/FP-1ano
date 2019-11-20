import math

N = int(input("Número: "))

def aproxPi(N):
	
	k = (math.pi/4) / (((-1)**N) / (2*N + 1))

	return k
	
print("Solução:",aproxPi(N))