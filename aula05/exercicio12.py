N = int(input("Número: "))

def fibonnacci(N):
	
	if N == 0:
		k = 0
	elif N == 1:
		k = 1
	else:
		x = 1
		y = 1
		i = 2

		while N >= i:
			k = y + x
			x = y
			y = k
			i += 1

	return k
	
print("Solução:",fibonnacci(N))
