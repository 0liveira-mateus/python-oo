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
    def get_titular(self):
        return self.__titular
    @property
    def limite(self):
        print("Limite de {}".format(self.__limite))
        return self.__limite
    @limite.setter
    def limite(self, valor):
        self.__limite = valor




conta_mateus = Conta(123, 'Mateus', 500, 1000)

conta_mateus.limite

conta_mateus.limite = 200

conta_mateus.limite