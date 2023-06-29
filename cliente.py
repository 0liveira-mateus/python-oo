class Cliente:
    def __init__(self, Nome):
        self.__nome = Nome

    @property
    def nome(self):
        print("Chamando")
        return self.__nome.title()
    @nome.setter
    def nome(self, nome):
        print("Chamando setter")
        self.__nome = nome

cliente = Cliente("mateus")


cliente.nome = 'Anicele'

cliente.nome

