tempo = float(input('Tempo em Segundos: '))

horas = tempo // 3600

minutos = (tempo % 3600) // 60

segundos = tempo - (horas * 3600 + minutos * 60)

print("%2.0f" % horas,':',"%2.0f" % minutos,':',"%2.0f" % segundos)
