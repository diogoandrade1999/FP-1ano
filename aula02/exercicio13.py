pc = 24.95
pf = 20
imp = 0.23
spa = 0.2

lucro = ((pc - spa) / (1 + imp)) - pf

lucrotiragem = 500 * lucro
impostos = pf * imp * 500
taxas = impostos + (0.2 * 500)

print("%.2f" % lucrotiragem,",","%.2f" % impostos,",","%.2f" % taxas)
