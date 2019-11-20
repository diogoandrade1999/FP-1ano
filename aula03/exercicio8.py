dia = int(input("Dia: "))
mes = int(input("MES: "))
ano = int(input("ANO: "))

bissexto = ano % 4
exepcao1 = ano % 100
exepcao2 = ano % 400

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
	if dia == 31:
		if mes == 12:
			diaa = dia - 1
			dias = 1
			mesa = mes
			mess = 1
			anoa = ano
			anos = ano + 1
		else :
			diaa = dia - 1
			dias = dia + 1
			mesa = mes
			mess = mes
			anoa = ano
			anos = ano
	elif dia == 1:
		if mes == 1:
			diaa = 31
			dias = dia + 1
			mesa = 12
			mess = mes
			anoa = ano - 1
			anos = ano
		if mes == 8:
			diaa = 31
			dias = dia + 1
			mesa = mes - 1
			mess = mes
			anoa = ano - 1
			anos = ano
		if mes == 3:
			if (bissexto == 0 and exepcao1 != 0) or exepcao2 == 0:
				diaa = 29
			else :
				diaa = 28
			dias = dia + 1
			mesa = mes - 1
			mess = mes
			anoa = ano
			anos = ano
		else :
			diaa = dia - 1
			dias = dia + 1
			mesa = mes - 1
			mess = mes
			anoa = ano
			anos = ano
	else :
		diaa = dia - 1
		dias = dia + 1
		mesa = mes
		mess = mes
		anoa = ano
		anos = ano
elif mes == 2:
	if (bissexto == 0 and exepcao1 != 0) or exepcao2 == 0:
		if dia == 29:
			diaa = dia - 1
			dias = 1
			mesa = mes
			mess = 3
			anoa = ano
			anos = ano
			
		elif dia == 1:
			diaa = 31
			dias = dia + 1
			mesa = 1
			mess = mes
			anoa = ano
			anos = ano
		else :
			diaa = dia - 1
			dias = dia + 1
			mesa = mes
			mess = mes
			anoa = ano
			anos = ano
	else :
		if dia == 28:
			diaa = dia - 1
			dias = 1
			mesa = mes
			mess = 3
			anoa = ano
			anos = ano
		
		elif dia == 1:
			diaa = 31
			dias = dia + 1
			mesa = 1
			mess = mes
			anoa = ano
			anos = ano
		else :
			diaa = dia - 1
			dias = dia + 1
			mesa = mes
			mess = mes
			anoa = ano
			anos = ano
else:
	if dia == 30:
		diaa = dia - 1
		dias = 1
		mesa = mes
		mess = mes + 1
		anoa = ano
		anos = ano
	elif dia == 1:
		diaa = 31
		dias = dia + 1
		mesa = mes - 1
		mess = mes
		anoa = ano
		anos = ano
	else :
		diaa = dia - 1
		dias = dia + 1
		mesa = mes
		mess = mes
		anoa = ano
		anos = ano

print("Dia Anterior: ",diaa,"/",mesa,"/",anoa)
print("Dia Seguinte: ",dias,"/",mess,"/",anos)
