x = float(input("x: "))
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

def polinomio(x, a, b, c):
	p = a * x**2 + b*x + c
	return p

print(polinomio(x, a, b, c))