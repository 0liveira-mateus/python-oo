class Datas:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    def formatar(self):
        print("{}/{}/{}".format(self.dia, self.mes, self.ano))


data = Datas(21, 11, 2007)

data.formatar()
