
# for number in range(-50,10,2):
	# print(number)

lista = [1,2,3,1,1,1,4,5,6,7,1,1,8,9]

while 1 in lista:
	# print(lista)
	lista.remove(1)

# print(lista)


## LIST COMPREHENSIONS
lista = [n*100 for n in range(10)]
print(lista)

letras = [l.lower() for l in 'jdnfkjsdnQHWHWDNIEsdkjbfQKJJSD']
print(letras)

matriz = [n for n in range(10) ]