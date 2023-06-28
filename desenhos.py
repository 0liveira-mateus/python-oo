class Desenho:
    def __init__(self, NomeCliente, Valor, Dia, mes, ano):
        self.__NomeDoCliente = NomeCliente,
        self.__Valor = Valor,
        self.__Dia = Dia
        self.__Mes = mes
        self.__Ano = ano
    def ImprimirDados(self):
        print('Pedido do Cliente {} de valor: {} realizado com sucesso, data de entrega: {}/{}/{} '.format(self.__NomeDoCliente,self.__Valor, self.__Dia, self.__Mes, self.__Ano))


DesenhoDoRyu = Desenho(NomeCliente='Mateus', Valor=0, Dia=27, mes=6, ano=2023)

mudando = DesenhoDoRyu

DesenhoDoRyu.ImprimirDados()
mudando.ImprimirDados()