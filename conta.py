class Conta:
    def __init__(self, numero, titular, saldo, limite): #init é uma função construntora
        print("Construindo Objeto {} ".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

conta = Conta(321, "Anicele", 100, 2000)

print(conta.saldo)