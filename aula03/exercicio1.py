api = float(input("API: ")) * 0.3
atp = float(input("ATP: ")) * 0.3
ep = float(input("EP: ")) * 0.4

nota = api + atp + ep

if nota >= 10:
	print("Aprovado")
else :
	print("Reprovado")
