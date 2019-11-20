x = float(input("X = "))
y = float(input("Y = "))

def maximo(x, y):
	 if x > y:
		 maxi = x
	 elif x < y:
		 maxi = y
	 else:
		 maxi = x
	 return maxi
	
print(maximo(x, y))
