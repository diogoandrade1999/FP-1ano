pistaMil = 10
tempoSeg = (43*60) + 30

tempHora = tempoSeg / 3600

pistaKm = pistaMil * 1.61

tempoMedio = tempHora / pistaKm

veloMedia = pistaKm / tempHora

print('Tempo Média:',"%4.2f" % tempoMedio)
print('Velocidade Média: ',"%4.2f" % veloMedia)
