import requests

response = requests.get('https://brasil.io/api/dataset/cursos-prouni/cursos/data')

lista = response.json()

print(lista['results'][0])



