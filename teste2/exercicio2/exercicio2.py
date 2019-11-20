def jogos_jornadas():
	jog = {}

	ficheiro = open('Jornadas.csv', 'r')

	for line in ficheiro:
		jornada, team_casa, team_visita = line.strip().split(',')
		jogo = (jornada, team_casa, team_visita)

		if jornada not in jog:
			jog[jornada] = []

		jog[jornada].append(jogo)

	ficheiro.close()

	return jog

def jogos_resultados():
	res = {}

	ficheiro = open('Jogos.csv', 'r')

	for line in ficheiro:
		data, team_casa, team_visita, res_casa, res_visita = line.strip().split(',')
		resultado = (data, team_casa, team_visita, res_casa, res_visita)

		if team_casa not in res:
			res[team_casa] = []

		res[team_casa].append(resultado)

	ficheiro.close()

	return res

def main():
	jogos = jogos_jornadas()
	resultados = jogos_resultados()

	while True:
		aposta = {}
		jornada = input("jornada? ")

		arquivo = 'Jornada' + jornada + '.csv'
		ficheiro = open(arquivo, 'w')

		if jornada in jogos.keys():
			for jogo in range(len(jogos[jornada])):
				verificacao = True

				while verificacao:
					print(jogo + 1, jogos[jornada][jogo][1], 'vs', jogos[jornada][jogo][2], ': ', end='')
					escolha = input()

					if escolha == '1':
						verificacao = False
					elif escolha == 'x':
						verificacao = False
					elif escolha == '2':
						verificacao = False

				ficheiro.write(str(jogo + 1)+', '+escolha+'\n')
				
				if str(jogo + 1) not in aposta:
					aposta[str(jogo + 1)] = []
				aposta[str(jogo + 1)].append(escolha)

		

			print()
			print("jornada", jornada)

			for jogo in range(len(aposta)):
				print("{} {:>10s} {:>1s} - {:<1s} {:<10s} : {}".format(jogo, resultados, res_casa, res_visita, team_visita,aposta[jogo] ))

		ficheiro.close()

main()