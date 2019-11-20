def verificacao(x):
	y = x[::-1]
	if x.upper() == y.upper():
		k = True
	else:
		k = False
	return k

x = input("Digite algo: ")
print(verificacao(x))