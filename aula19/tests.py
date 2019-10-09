def soma(numero1, numero2):
    if validador(numero1) and validador(numero2):
        return numero1 + numero2

def validador(numero):
    return type(numero) in [int, float]

def test_soma():
    assert soma(2,2) == 4

def test_soma_numero_negativo():
    assert soma(2,-2) == 0

def test_valida_numero():
    assert not validador('x')

def test_valida_numero_real():
    assert validador(2.4)

def test_soma_reais():
    assert soma(2.5,'x') == None


import pdb
pdb.set_trace()

soma1 = soma(10, 20)
soma2 = soma(110, 'Mario')
soma3 = soma(-1, -200)

resultado = soma1+soma2+soma3
# raise Exception("TestError 123")

# try:
#     10/0
# except ZeroDivisionError:
#     print("divisor igual a zero")
