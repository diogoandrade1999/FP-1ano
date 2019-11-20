x1 = int(input("x do ponto 1: "))
y1 = int(input("y do ponto 1: "))
x2 = int(input("x do ponto 2: "))
y2 = int(input("y do ponto 2: "))

x = x2 - x1
y = y2 - y1

distancia = float(((x ** 2) + (y ** 2)) ** (1/2))

print("Distancia entre os dois pontos é:","%.2f" % distancia)


