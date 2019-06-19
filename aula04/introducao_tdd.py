import unittest
import string

# normal:  abcdefghijklmnopqrstuvwxyz
# cifrado: defghijklmnopqrstuvwxyzabc

# normal:  a ligeira raposa marrom saltou sobre o cachorro cansado
# cifrado: d oljhlud udsrvd pduurp vdowrx vreuh r fdfkruur fdqvdgr

# 4 casas para frente

def cifra(frase):
    frase_alterada = ''
    for letra in frase:
        frase_alterada += cifra_letra(letra)

    return frase_alterada 

def cifra_letra(letra):
    alfabeto = string.ascii_lowercase #lista de strings
    indice =  alfabeto.find(letra)
    if indice==-1:
        return ' ' 
    return alfabeto[(indice + 3)%len(alfabeto)]

 
class TestCesarMethods(unittest.TestCase):
    
    def test_cifra_a(self):
        self.assertEqual(cifra_letra('a'), 'd')

    def test_cifra_c(self):
        self.assertEqual(cifra_letra('c'), 'f')

    def test_cifra_z(self):
        self.assertEqual(cifra_letra('z'), 'c')

    def test_cifra_x(self):
        self.assertEqual(cifra_letra('x'), 'a')

    def test_palavra(self):
        self.assertEqual(cifra("abcdefghijklmnopqrstuvwxyz"), "defghijklmnopqrstuvwxyzabc")

    def test_palavra_espaco(self):
        self.assertEqual(cifra("a ligeira raposa"), "d oljhlud udsrvd")
if __name__ == '__main__':
    unittest.main()
