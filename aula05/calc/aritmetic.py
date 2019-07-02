def soma(num1, num2):
	return num1+num2

def mult(num1, num2):
	return num1*num2


def fat_recursive(numero):
	if numero == 0:
		return 1
	return numero*fat_recursive(numero-1)

def fat_loop(numero):
	resultado = 1
	while numero >= 1:
		resultado = resultado*numero
		numero -= 1
	return resultado

print(fat_recursive(4))
print(fat_loop(4))