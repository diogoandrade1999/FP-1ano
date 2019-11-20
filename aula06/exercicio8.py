x = input("Digite algo: ")
y = ''

for i in x.upper().split():
	if len(i) > 2 and len(y) <= 3:
		y = y + i[0]
print(y)