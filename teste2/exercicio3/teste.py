import sys
print('Number of args:', len(sys.argv), 'arguments.')
print('Argument List:', sys.argv)

import os
diretorio = input("direrotio: ")
extensao = input("extensao: ")
for root, dirs, files in os.walk(diretorio, topdown=False):
	for name in files:
		print(os.path.join(root, name))
		if root == diretorio and extensao == name.split('.')[1]:
			print(os.path.join(root, name))
	for name in dirs:
		print(os.path.join(root, name))

L = [9, 7, 2, 8, 5, 3]
L.sort() # Modifies L in-place
print(L)
L2 = sorted(L) # Creates L2. L is not modified!
print(L2)
L = [9, 7, 2, 8, 5, 3]
print(sorted(L))
#-> [2, 3, 5, 7, 8, 9]
L = ["maria", "carla", "anabela", "antonio", "nuno"]
print(sorted(L))
#-> ['anabela', 'antonio', 'carla', 'maria', 'nuno']
L = ["Mario", "Carla", "anabela", "Maria", "nuno"]
print(sorted(L)) # lexicographic sort
#-> ['Carla', 'Maria', 'Mario', 'anabela', 'nuno']
print(sorted(L, key=len)) # sort by length
#-> ['nuno', 'Mario', 'Carla', 'Maria', 'anabela']
print(sorted(L, key=str.lower))
#-> ['anabela', 'Carla', 'Maria', 'Mario', 'nuno']
dates = [(1910, 4, 25, 'Republic'),(1974, 4, 5, 'Liberty'),(1640, 12, 1, 'Independence')]
print(sorted(dates)) # "lexicographic" order
print(sorted(dates, key=lambda t: t[3])) #by name
print(sorted(dates, key=lambda t:(t[1],t[2]))) #by month,day