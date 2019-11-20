X = int(input("X= "))
Y = int(input("Y= "))

def euclides(X, Y):
	if X >= Y:
		a = X
		b = Y
	else:
		a = Y
		b = X
	
	z = a // b
	
	return z
	
print("m.d.c.=",euclides(X, Y))
