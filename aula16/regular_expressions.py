import re

cpf_mario = '031.825.491-39'

cpf_pattern = '[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}'

cpf_validate_true = re.search(cpf_pattern, cpf_mario)
cpf_validate_false = re.search(cpf_pattern, '031.82.49139')

print(cpf_validate_true.group())
print(cpf_validate_false)


with open('../aula14/data.csv') as file:
	strings = re.findall('Florianópolis', file.read())
	print(len(strings))
