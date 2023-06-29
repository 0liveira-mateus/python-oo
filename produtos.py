class Produto:

    def __init__(self, codigo, preco, quantidade):
        self.__codigo = codigo
        self.__preco = preco
        self.__quantidade = quantidade
    def get_quantidade(self):
        return self.__quantidade
    def set_quantidade(self, valor_novo):
        self.__quantidade = valor_novo
    def adicionar(self, quantidade_nova):
        self.__quantidade += quantidade_nova



produto1 = Produto(123, 500, 1)

produto1.set_quantidade(300)

print(produto1.get_quantidade())


produto1.adicionar(100)

print(produto1.get_quantidade())



