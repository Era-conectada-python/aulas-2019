text = "paralelepípedo"

for letra in text:
	if letra == 'a':
		print(letra*2)
	else:
		print("Não é a letra 'a'")


var = input()

print("O número é {}".format(var))

meses = {1: 'Janeiro',
		 2: 'Fevereiro',
		 3: 'Março',
		 4: 'Abril',
		 5: 'Maio',
		 6: 'Junho',
		 7: 'Julho',
		 8: 'Agosto',
		 9: 'Setembro',
		 10: 'Outubro',
		 11: 'Novembro',
		 12: 'Dezembro',
		 }

data = input('Data: ').split('/')

output = [data[0], meses[int(data[1])], data[2]]

print('Data de Nascimento: {} de {} de {}'.format(*output))