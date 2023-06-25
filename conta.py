
def criarconta(Numero, titular, saldo, limite):
    conta = {'Numero': Numero, "titular": titular, "saldo":saldo, "limite": limite}
    return conta


def depositar(conta, valor):
    conta['saldo'] += valor


def sacar(conta, valor):
    conta['saldo'] += valor

def extrato(conta):
    print("O saldo da é conta é {}".format(conta['saldo']))

conta_anicele = criarconta(25, "Anicele", 1000, 20000)

print(conta_anicele)

depositar(conta_anicele, 200)

extrato(conta_anicele)