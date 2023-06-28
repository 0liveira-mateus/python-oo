class Conta:
    def __init__(self, numero, titular, saldo, limite): #init é uma função construntora
        print("Construindo Objeto {} ".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    def extrato(self):
        print("Olá {}, seu saldo é: {}".format(self.__titular, self.__saldo))
    def sacar(self, valor):
        self.__saldo -= valor
    def depositar(self, valor):
        self.__saldo += valor

conta_Mateus = Conta(2112, "Mateus", 700, 360)

saque = float(input("Quanto vc deseja sacar?"))

conta_Mateus.sacar(saque)

conta_Mateus.extrato()

deposito = float(input("Quanto vc deseja depositar?"))

conta_Mateus.depositar(deposito)

conta_Mateus.extrato()

