class Pessoa():
    def __init__(self, nome, endereco, cpf):
        self.nome = nome
        self.endereco = endereco
        self.cpf = cpf

    def __falar__(self):
        return 'Pessoa falando'

    def contar_piada(self):
        print(self.__falar__() + ' Piada')



pessoa_1 = Pessoa('Mario Sergio', 'Lagoa', '03182549136')

# pessoa_1.contar_piada()

# HERANÇA

class Funcionario(Pessoa):
    def __init__(self, nome, endereco, cpf, matricula, departamento):
        super().__init__(nome, endereco, cpf)
        self.matricula = matricula
        self.departamento = departamento

f = Funcionario(nome='João', endereco='Beira Mar',
                cpf='4234423234', matricula=1, departamento='financeiro')

# f.contar_piada()

# POLIMORFISMO

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, raça):
        self.raça = raça
        self.som = ''
        self.__pelo = 'liso'

    @abstractmethod
    def função():
        pass

    def emitir_som(self):
        print(f'O {self.raça} emite o som: {self.som}')

    def imprimir_pelo(self):
        print(self.__pelo)

class Cachorro(Animal):
    def função(self):
        print('Vigilante')

class Gato(Animal):
    def função(self):
        print('Caçador')

dogzera = Cachorro('Pastor Alemão')
dogzera.som = 'Au au!'
dogzera.emitir_som()
dogzera.função()
dogzera.imprimir_pelo()

catzera = Gato('Siamês')
catzera.som = 'Miau!'
catzera.emitir_som()
catzera.função()


