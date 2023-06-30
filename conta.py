class Conta:
    def __init__(self, numero, titular, saldo, limite): #init é uma função construntora
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    def extrato(self):
        print("Olá {}, seu saldo é de: {} reais".format(self.__titular, self.__saldo))
    def pode_sacar(self, valor):
        if valor <= self.__saldo + self.__limite:
            print("Sancando R${} reais". format(valor))
        else:
            print("Valor indisponivel para sacar")
    def sacar(self, valor):
        self.pode_sacar(valor)
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
    @staticmethod
    def codigoBanco():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

conta_mateus = Conta(123, 'Mateus', 500, 1000)

print(conta_mateus.get_saldo())

conta_mateus.sacar(12)

codigos = Conta.codigoBanco()


print(codigos['Caixa'])