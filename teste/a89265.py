#Diogo André Lopes Andrade 89265

massa = float(input("Massa (kg)? "))
velocidade = float(input("Velocidade (m/s)? "))

energia = 0.5 * massa * velocidade**2

print("Energia cinética do corpo: ",energia)

if energia < 1000:
	print("Baixa")
elif 1000 <= energia <= 5000:
	print("Média")
else:
	print("Alta")
