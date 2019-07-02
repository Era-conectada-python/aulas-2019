# from utils import name_to_list, name_to_tuple
# from utils import *
import utils

# from calc.aritmetic import soma, mult
from calc import aritmetic 


numero = 5

def func(numero):
	numero = 50
	if numero < 10:
		numero = 10
		print(numero)
	else:
		print(numero/2)

	numero_real = 100.97
	return numero_real

print(func(numero))


def func_division(numero1, numero2):
	if numero1 > numero2:
		return numero1/numero2, numero1%numero2, numero1//numero2
	return numero2/numero1, numero2%numero1, numero2//numero1


divisao, modulo, divisao_inteira = func_division(10, 20)
print(divisao, modulo, divisao_inteira)


def imprime_nome(nome, sobrenome="<sem sobrenome>"):
	print("O nome é {} {} que é brasileiro".format(nome, sobrenome))

# nome = input("Digite o nome: ")
# sobrenome = input("Digite o sobrenome: ")
# imprime_nome(nome)

print(utils.name_to_list("Mário"))
print(utils.name_to_tuple("Mário"))

print(aritmetic.soma(1,1))
print(fileX.soma(1,1))

