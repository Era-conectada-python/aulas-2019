import urllib3
from bs4 import BeautifulSoup

import unittest

url = "https://economia.uol.com.br/cotacoes/cambio/dolar-comercial-estados-unidos/"
http = urllib3.PoolManager()
headers = {'Connection': 'keep-alive'} 
page = http.request('GET', url, headers = headers)
soup = BeautifulSoup(page.data, 'html.parser')

def cotacao_data(date):

	tabela = soup.find_all('tr')
	print(tabela)





class TestDolarMethods(unittest.TestCase):
    
    def test_cotacao_data(self):
        self.assertEqual(cotacao_data('24.09.2019'), 4.1632)

if __name__ == '__main__':
    unittest.main()

