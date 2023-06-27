class Conta:
    def __init__(self, numero, titular, saldo, limite): #init é uma função construntora
        print("Construindo Objeto {} ".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    def extrato(self):
        print("Olá {}, seu saldo é: {}".format(self.titular, self.saldo))
    def sacar(self, valor):
        self.saldo -= valor

conta_Mateus = Conta(2112, "Mateus", 700, 360)

saque = float(input("Quanto vc deseja sacar?"))

conta_Mateus.sacar(saque)

conta_Mateus.extrato()
