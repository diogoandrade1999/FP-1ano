peso = float(input("Peso (kg): "))
altura = float(input("Altura (metros): "))

def Imc():
	imc = peso / (altura * altura)
	return imc

print(Imc())