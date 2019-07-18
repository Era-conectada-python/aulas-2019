import unittest


# CONSTRUIR DICIONARIOS INTERNACIONAIS DE NÚMEROS (pt-br, en-us, es-es)
# Ex: (2, 'pt-br') -> 'dois'

dic_linguas = {
'pt_br': {'one': 'um', 'two': 'dois', 'three': 'tres'},
'en_us': {'one': 'one', 'two': 'two', 'three': 'three'},
'es_es': {'one': 'uno', 'two': 'dos', 'three': 'tres'}
}

def int_to_text(number):
    numbers = {1:"one",2:'two',3:'three'}
    return numbers[number]

def traducao(number, language):
    key = int_to_text(number)
    return dic_linguas[language][key]
    



class TesteDicLinguas(unittest.TestCase):
    
    def test_pt_br(self):
        self.assertTrue('pt_br' in dic_linguas)

    def test_en_us(self):
        self.assertTrue('en_us' in dic_linguas)

    def test_es_es(self):
        self.assertTrue('es_es' in dic_linguas)

    def test_inteiro(self):
        self.assertEqual(int_to_text(1),"one")

    def test_traducao(self):
        self.assertEqual(traducao(1,'pt_br'), 'um')

if __name__ == '__main__':
    unittest.main()