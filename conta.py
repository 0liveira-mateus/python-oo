class Conta:
    def __init__(self, numero, titular, saldo, limite): #init é uma função construntora
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    def extrato(self):
        print("Olá {}, seu saldo é de: {} reais".format(self.__titular, self.__saldo))
    def sacar(self, valor):
        self.__saldo -= valor
    def depositar(self, valor):
        self.__saldo += valor
    def transferir(self, valor, conta2):
        self.sacar(valor)       # basicamente diz: dentro desse objeto, chame a função sacar
        conta2.depositar(valor)
# Get só retorna um valor, set atribui um novo valor aquele atributo
    def get_saldo(self):
        return self.__saldo
    def get_limite(self):
        return self.__limite
    def set_limite(self, valor):
        self.__limite = valor



conta_mateus = Conta(123, 'Mateus', 500, 1000)
conta_anicele = Conta(321, 'Anicele', 700, 2000 )

conta_mateus.extrato()
conta_anicele.extrato()

conta_mateus.transferir(100, conta_anicele)

print("-----------------------------------")

conta_mateus.extrato()
conta_anicele.extrato()

print("-----------------------------------")

print(conta_mateus.get_limite())
print(conta_anicele.get_limite())

conta_mateus.set_limite(3000)
conta_anicele.set_limite(4000)

print("-----------------------------------")

print(conta_mateus.get_limite())
print(conta_anicele.get_limite())

