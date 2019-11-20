mes = int(input("MES: "))
ano = int(input("ANO: "))

bissexto = ano % 4
exepcao = ano % 100

if ano == 2000:
	exepcao = 1

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
	print("31 Dias")
elif mes == 2:
	if bissexto == 0 and exepcao != 0:
		print("29 Dias")
	else :
		print("28 Dias")
else:
	print("30 Dias")
