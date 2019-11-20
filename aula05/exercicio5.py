x = float(input("X = "))
y = float(input("Y = "))
z = float(input("Z = "))

def maximo(x, y, z):
	 if x >= y and x >= z:
		 maxi = x
	 elif y >= x and y >= z:
		 maxi = y
	 else:
		 maxi = z
	 return maxi
	
print(maximo(x, y, z))
