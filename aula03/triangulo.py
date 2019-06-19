l1 = 3
l2 = 3
l3 = 3

# verificar se algum dos é menor ou igual a zero
if l1<=0 or l2<=0 or l3<=0:
	print("Não são dimensões de um triângulo")
	quit()

# verificar se realmente é um triângulo
if l1>=l2+l3 or l2>=l1+l3 or l3>=l2+l1:
	print("Não são dimensões de um triângulo")
	quit()

if l1==l2 and l2==l3:
	print("Equilatero")
elif :