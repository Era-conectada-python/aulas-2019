arquivo = open('pib.csv', 'r')

conteudo = arquivo.readlines()

for line in conteudo:
	print(line[:-1])

anos = [l.split(',')[0] for l in conteudo[1:]]
print(anos)

arquivo.close()