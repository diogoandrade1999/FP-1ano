x = float(input("LITROS: "))

if x <= 40:
	y = x * 1.4
	print(y)
else :
	y = x * 1.4 - x * (1.4 * 0.1)
	print("%.2f" % y)
