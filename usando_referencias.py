class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

ana = Funcionario("Ana", 5000)
joaquim = ana
joaquim.salario = 2500

print(joaquim.nome)
print(joaquim.salario)
print(ana.nome)