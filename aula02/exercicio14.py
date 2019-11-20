tempo1 = 10 * 1
tempo2 = 6 * 3
tempo3 = (1+3) * 10

tempomin = tempo1 + tempo2 + tempo3

tempototal = (60 * 6) + 52 + tempomin

horas = tempototal // 60

minutos = tempototal % 60

print(horas,":",minutos)
