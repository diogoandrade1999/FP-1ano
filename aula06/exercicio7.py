x = input("Digite algo: ")

def countDigits(x):
	y = 1
	for i in x:
		if i == ' ':
			y += 1
	return y

print("Tem {} digitos.".format(countDigits(x)))