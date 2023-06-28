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
        self.sacar(valor)
        conta2.depositar(valor)


conta_mateus = Conta(123, 'Mateus', 500, 1000)
conta_anicele = Conta(321, 'Anicele', 700, 2000 )

conta_mateus.extrato()
conta_anicele.extrato()

conta_mateus.transferir(100, conta_anicele)

print("-----------------------------------")

conta_mateus.extrato()
conta_anicele.extrato()
