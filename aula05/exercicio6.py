r = float(input("r= "))

def tax(r):
	if r <= 1000:
		tax = 0.1 * r
	elif 1000 < r <= 2000:
		tax = 0.2 * r - 100
	else:
		tax = 0.3 * r - 300
	return tax
	
print("%.2f" % tax(r))
