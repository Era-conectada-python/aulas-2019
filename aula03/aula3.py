try:
    numero = int(input("Digite um numero ímpar: "))
    if type(numero) == int:
        print(numero)

except(ValueError):
    print("Valor não inteiro.")

numeros = [2,5,10,23,100]

for numero in numeros:
    if numero%2!=0 and numero > 10:
        print(numero, 'Ímpar e maior que 10')
    elif numero%2!=0:
        print(numero, 'Ímpar')
    else:
        print(numero, 'Par')

count = 0
while count < 10:
    if count == 5:
        break
    print(count)
    count += 1
