import csv


tupla = (1,2,3,4)
lista = list(tupla)

csv_file = "names.csv"
csv_columns = ['Name','Country']
data = [
{'Name': 'Alex', 'Country': 'India'},
{'Name': 'Ben', 'Country': 'USA'},
{'Name': 'Shri Ram', 'Country': 'India'},
{'Name': 'Smith', 'Country': 'USA'},
{'Name': 'Yuva Raj', 'Country': 'India'},
]

for x in range(3):
    name = input('Digite seu nome: ')
    country = input('Digite seu país: ')
    data.append({'Name': name, 'Country': country})

with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for element in data:
        writer.writerow(element)


dicionario = {'um': 1,
              'dois': 2,
              'tres': 3,
              'quatro': 4,
}

for index in dicionario.keys():
    print(index)

for value in dicionario.values():
    print(value)

for item in dicionario.items():
    print(item)

for index, item in enumerate(dicionario):
    print(index, item)

if 'dois' in dicionario:
    print(dicionario['dois'])

